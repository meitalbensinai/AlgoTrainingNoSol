import json
import os
import glob
from utils.Test import get_official_solution, test

if __name__ == '__main__':
    with open(f'{os.getcwd()}\\time_limits.json', 'r') as f:
        time_limits = json.load(f)

    with open(f'{os.getcwd()}\\time_limits.json', 'w') as f:
        no_limit = {k: 30 for k in time_limits.keys()}
        json.dump(no_limit, f)

    for i, problem_name in enumerate(time_limits.keys()):
        print('----------------------------------------------------------------')
        print(f'{i+1}.{problem_name}')
        print('----------------------------------------------------------------')

        solution = get_official_solution(problem_name)
        test_amount = len(glob.glob(f'{os.getcwd()}\\inputs\\{problem_name}\\*.json'))
        max_time = 0
        for idx in range(1, test_amount + 1):
            time_needed = test(problem_name, idx, solution)
            max_time = max(max_time, time_needed)
        time_limits[problem_name] = max(time_limits[problem_name], max_time + 0.05)

    with open(f'{os.getcwd()}\\time_limits.json', 'w') as f:
        json.dump(time_limits, f)

    print('Done!')
