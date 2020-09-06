import glob
import importlib
import multiprocessing
from typing import Callable, Tuple
import numpy as np
import json
import time
import os

INPUTS_PATH = f'{os.getcwd()}\\inputs'
MAX_TEST_AMOUNT = 10


def get_input(problem_name: str, idx: int) -> Tuple:
    path = f'{INPUTS_PATH}\\{problem_name}\\test_{idx}.json'
    if f'test_{idx}.json' not in os.listdir(f'{INPUTS_PATH}\\{problem_name}'):
        raise FileNotFoundError('Test index does not exist')
    with open(path, 'r') as f:
        arguments = json.load(f)
    if not arguments['visible']:
        raise PermissionError('The requested test is not visible')
    return arguments['arguments']


def wrapper(func, return_dict, *args, **kwargs):
    initial_time = time.time()
    output = func(*args, **kwargs)
    end_time = time.time()
    time_needed = np.round(end_time - initial_time, 2)
    return_dict['time_needed'] = time_needed
    return_dict['output'] = output


def get_solution(problem_name: str) -> Callable:
    problem_name = problem_name.replace(" ", "_")
    path = f'problems.{problem_name}'
    file = '.' + problem_name.title().replace("_", "")
    sol = importlib.import_module(file, path)

    module = problem_name + '_solution'
    return getattr(sol, module)


def get_official_solution(problem_name: str) -> Callable:
    try:
        problem_name = problem_name.replace(" ", "_")
        path = f'problems.{problem_name}'
        file = '.' + problem_name.title().replace("_", "") + 'Solved'
        sol = importlib.import_module(file, path)

        module = problem_name + '_solution'
        return getattr(sol, module)
    except FileNotFoundError:
        print('No access to official solution')


def test(problem_name: str, idx: int, solution: Callable) -> int:
    # Start bar as knapsack process
    try:
        problem_name = problem_name.replace("_", " ")
        path = f'{INPUTS_PATH}\\{problem_name}\\test_{idx}.json'
        with open(path, 'r') as f:
            data = json.load(f)
            arguments = data['arguments'].values()
            desired_output = data['desired_output']
        with open(f'{os.getcwd()}\\time_limits.json', 'r') as f:
            data = json.load(f)
            time_limit = data[problem_name]
    except:
        raise FileNotFoundError('Test index does not exist')
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    p = multiprocessing.Process(target=wrapper, args=(solution, return_dict, *arguments))
    print('Starting')
    p.start()

    # give the solution the given time to run
    p.join(time_limit + 1)

    # If thread is still active
    if p.is_alive() or return_dict['time_needed'] > time_limit:
        print('Time limit exceeded. You can do better than that!')

        # Terminate
        p.terminate()
        p.join()
        return time_limit

    time_needed = return_dict['time_needed']
    output = return_dict['output']
    if desired_output == output:
        print(f'Well done! test #{idx} had been passed successfully.')
        print(f'Time required: {time_needed} seconds.')
        return time_needed
    else:
        print('Solution is incorrect.')
        return time_limit


def test_all(problem_name: str, solution: callable) -> None:
    problem_name = problem_name.replace("_", " ")
    tests = glob.glob(f'{INPUTS_PATH}\\{problem_name}\\*.json')
    for idx in range(1, len(tests) + 1):
        test(problem_name, idx, solution)
