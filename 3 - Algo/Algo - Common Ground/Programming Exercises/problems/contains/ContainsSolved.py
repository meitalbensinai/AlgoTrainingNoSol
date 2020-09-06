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
from shapely.geometry import Polygon, LineString, Point
import numpy as np


def contains_solution(vertices: List[Tuple[float, float]], points: List[Tuple[float, float]]) -> List[bool]:
    """ Check for every point if the given polygon contains it or not

    :param vertices: the vertices of the polygon. it is assured that all coordinates are 2D, and the vertices are sorted
    clockwise.
    :param points: list of points for examination
    :return: mask representing for every point if it's inside the polygon
    """

    """
    idea:
    for every point, we create an infinite* line from to right, and we count the amount of times this line intersects
    the boundary of the polygon. if this amount of times is even it means the point is outside the polygon, and if odd
    then it's inside.
    *since whe know the vertices of the polygon the line doesn't have to be infinitely long, just pass the rightmost
    vertex.
    *an exceptional rule is where one of the intersections is with a vertex and not and edge. while intersections with
    an edge changes the inside/outside state of the line, intersection with a node might so it, but also might keep the
    previous state. in order to check it, we check id the previous and next vertices are in different sides of our line
    (state is changes, like crossing an edge) or that they are both on the same side (state doesn't change). this can be
    checked by comparing the y values of the vertices.
    
    """

    p = Polygon(vertices)
    n = len(vertices)
    max_x_value = np.max([vertex[0] for vertex in vertices]) + 1
    output = []
    for point in points:
        amount = 0
        horizontal_line = LineString([point, (max_x_value, point[1])])
        intersections = horizontal_line.intersection(p.boundary)
        try:
            amount = len(intersections)
            for intersection_point in intersections:
                intersection = list(intersection_point.coords[0])
                if intersection in vertices:
                    idx = vertices.index(intersection)
                    if not vertices[idx - 1][1] < intersection[1] < vertices[(idx + 1) % n][1] \
                            and not vertices[(idx + 1) % n][1] < intersection[1] < vertices[idx - 1][1]:
                        amount -= 1
        except:  # if there are 0-1 intersections
            if isinstance(intersections, Point):
                amount = 1
                intersection = list(intersections.coords[0])
                if intersection in vertices:
                    idx = vertices.index(intersection)
                    if not vertices[idx - 1][1] < intersection[1] < vertices[(idx + 1) % n][1] \
                            and not vertices[(idx + 1) % n][1] < intersection[1] < vertices[idx - 1][1]:
                        amount -= 1

        output.append(int(amount % 2) == 1)
    return output
