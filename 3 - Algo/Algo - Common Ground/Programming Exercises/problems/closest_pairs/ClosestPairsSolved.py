"""
problem formalization:

You are given a list of numbers of even length - 2n. Divide the numbers into n pairs, such that the difference between
the sum of the pair with the highest sum to the sum of the pair with the lowest sum is minimal.

Create an EFFICIENT algorithm to perform the given task.


***
In addition:

prove the optimality of your solution.
***

-----------------------------------------------------------------------------------------------------------------------

Example:

input: [4, 7, 11, 18]
output: 4

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 0.2 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 5 test:
- tests 1-3 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 4-5 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List
import numpy as np


def closest_pairs_solution(a: List[float]) -> int:
    """ Finds the smallest multiple of n, made only of given set of digits

    :param a: list of numbers
    :return: the minimal sum-difference between the pair with highest sum to the pair with lowest sum
    """

    """
    idea:
    the optimal solution will be to sort the list and then match the maximum with the minimum and so on.
    """

    a.sort()
    a = np.array(a)
    pairs_sums = a + np.flip(a)
    minimal_sum = np.min(pairs_sums)
    maximal_sum = np.max(pairs_sums)
    return maximal_sum - minimal_sum
