"""
problem formalization:

given a polygon and a set of points, determine for each point if it's inside the polygon or not.
NOTE - you are allowed to use shapely objects (for example Polygon), as long as you do not use Polygon.contains
directly.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: [(0, 0), (0, 1), (1, 1), (1, 0)], [(2, 4), (0.5, 0.5)]
output: [False, True]

-----------------------------------------------------------------------------------------------------------------------


Limitations:

time - 0.1 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 3 test:
- tests 1-2 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 3 is not visible to you, and need to pass it without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List, Tuple
import shapely


def contains_solution(vertices: List[Tuple[float, float]], points: List[Tuple[float, float]]) -> List[bool]:
    """ Check for every point if the given polygon contains it or not

    :param vertices: the vertices of the polygon. it is assured that all coordinates are 2D, and the vertices are sorted
    clockwise.
    :param points: list of points for examination
    :return: mask representing for every point if it's inside the polygon
    """
    pass
