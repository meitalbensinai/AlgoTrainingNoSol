"""
problem formalization:

You are given 2 arrays:
1. A, N-sized integers array.
2. B, N-sized binary array.
The values of A are constant, but you are allowed to change the values of B by performing a double bit switch (DBS):
In a double bit switch, you choose two adjacent bits in B and perform NOT operation on both of them (reminder: NOT(0)
= 1, NOT(1) = 0).
You can use the the double bit switch operation as many times as you want.

Create an EFFICIENT algorithm to find the maximum value of dot product A*B that can be achieved by performing the DBS
operation over B.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: A = [-8, 12, 27, 4, 13, -8, 6], B = [1, 0, 1, 1, 0, 0, 1]
output: 58

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 0.15 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with out given input by 'CheckSolution' file.
You have a total of 4 test:
- tests 1-3 are visible to you, and you can access it's input using 'get_input' method from utils.Test.
- test 4 is not visible to you, and need to pass it without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List
import numpy as np


def double_bit_switch_solution(a: List[int], b: List[bool]) -> int:
    """ Decides which items to take, by maximizing the total value of them

    :param a: list of integers
    :param b: list of booleans
    :return: maximal possible dot-product value that can be obtained by performing DBSs.
    """

    """
    idea:
    We can notice that we can perform Not on any couple of bits (even if not adjacent) by performing DBS over all the
    adjacent bits between them. Therefore, the only invariant of B is the parity (is the amount of 1's even or odd).
    
    So, we will try to maximize the dot-product by substituting 1 at every bit in B corresponding to positive number in
    A, and 0 otherwise. if the parity fails, we flip the value of the bit corresponding to the smallest (absolute value)
    in A.
    """

    initial_parity = np.sum(b) % 2
    new_parity = 0
    min_value = np.inf
    s = 0

    for value in a:

        min_value = min(min_value, np.abs(value))
        if value > 0:
            s += value
            new_parity += 1

    new_parity = new_parity % 2
    return s if new_parity == initial_parity else s - min_value
