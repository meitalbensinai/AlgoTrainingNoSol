"""
Here you test your code performances.

We created several inputs to test your solution. Some of them are visible to you for debugging, and some are not.
the given inputs test your solution under time limitations - as describes in the problem file.

--ENTER THE RELEVANT PARAMETERS IN THE RUNNING CONFIGURATION--

Good luck!
"""
import argparse

from utils.Test import test, get_official_solution, test_all, get_solution, get_input

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest='problem_name', help='problem name: lowercase with underscores')
    parser.add_argument('-i', dest='test_idx', help='required test idx', required=False)

    args = parser.parse_args()
    solution = get_official_solution(args.problem_name)
    if args.test_idx:
        test(problem_name=args.problem_name, idx=args.test_idx, solution=solution)
    else:
        test_all(problem_name=args.problem_name, solution=solution)
