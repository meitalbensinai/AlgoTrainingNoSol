"""
problem formalization:

you want to put an advertisement poster over a block of buildings. the block is made of several buildings with different
heights. you can use as many (consecutive) building as you would like, as long as the height of the poster doesn't
exceed the height of the buildings. find the largest possible area you can use for your poster.
note - the width of every building is 1.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: heights = [1, 2, 3, 4]
output: 6
explanation - the poster will be hang from the second building to the last one (width 3) with height 2 (which is the
maximal possible height that does not exceed any of the building heights). notice that this is not the only way to
achieve this value, yet it's the maximal one.

-----------------------------------------------------------------------------------------------------------------------


Limitations:

time - 0.2 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 10 tests:
- tests 1-5 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 6-10 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List


def poster_solution(heights: List[float]) -> float:
    """ Finds the biggest possible poster area

    :param heights: the height of every building, according to their position
    :return: the biggest possible poster area
    """
    pass
