"""
problem formalization:

you are given a list of strings. we say that 2 strings can be chained if the last letter of one of them is the first
letter of the next one ('hola', 'angle' -> 'holangle'). Check if the list of strings (in any order) can be chained in
a circle (every string can be chained to the next one, and the last string can be chained to the first one).

Create an EFFICIENT algorithm to solve the task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: ['banana', 'apple', 'egb']
output: True

input: ['sharon', 'itay', 'ziv']
output: False

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 0.1 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with out given input by 'CheckSolution' file.
You have a total of 6 test:
- tests 1-3 are visible to you, and you can access it's input using 'get_input' method from utils.Test.
- test 4-6 is not visible to you, and need to pass it without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List


def string_chain_solution(lst: List[str]) -> bool:
    """ Checks if the list of string can be chained

    :param lst: list of lowercase no-spaces strings
    :return: True if chaining is possible else False
    """
    pass
