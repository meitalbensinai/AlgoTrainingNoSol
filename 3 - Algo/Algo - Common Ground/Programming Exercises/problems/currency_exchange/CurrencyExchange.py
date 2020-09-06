"""
problem formalization:

"In economics and finance, arbitrage is the practice of taking advantage of a price difference between two or more
markets" (Wikipedia).
In practice, we will be talking about arbitrage in currency exchange - where by only converting some currencies, we can
increase the value of the money we hold. For example, if 1 dollar can be converted to 3.54 NIS, and NIS can be converted
to 0.29 dollars, than by a chain of converts we can convert: 1 dollar -> 3.54 NIS -> 1.0266 dollars, and increase our
money worth.

given the convert table between N different currencies, determine whether an Arbitrage is possible.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: [[1, 3.54],
        [0.29, 1]]
output: True

-----------------------------------------------------------------------------------------------------------------------


Limitations:

time - 2 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 6 test:
- tests 1-4 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 5-6 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List


def currency_exchange_solution(t: List[List[float]]) -> bool:
    """ Determine if an arbitrage is possible

    :param t: table for converting between currencies. if t[i][j] = x, it means that 1 of current i equals x of
    currency j.
    :return: True if an arbitrage is possible, else False
    """
    pass
