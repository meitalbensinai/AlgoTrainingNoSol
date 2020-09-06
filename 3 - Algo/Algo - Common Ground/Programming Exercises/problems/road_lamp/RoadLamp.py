"""
problem formalization:

you are helping to re-plan lamps' location over a road. Initial planners had lower budget than they expected, so as you
drive the road you can see that the distances between lamps becomes monotonically increasing.
for specific road, you know that there are already N lamps along thw way, in given locations (distances from the start
of the road), you are allowed to add another K lamps in whatever locations you desire. your purpose is to make the road
as safe as possible by reducing the maximum distance between 2 lamps along the road as much as you can.
NOTICE!! that due to logistics reasons, lamps (old as new together) can only be located at integer distance from the
beginning of the road.

you can assume the original planner had put lamp in the beginning of the road and another one just where it ends,
so additional lamps will only be between the existing lamps.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: loc = [0, 4, 12], K = 1
output: 4
explanation - we add a new lamp at location 8, and therefore the maximal distance between lamps is 4.

-----------------------------------------------------------------------------------------------------------------------


Limitations:

time - 0.2 seconds

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


def road_lamp_solution(loc: List[int], k: int) -> int:
    """ Adds lamps to the road to make it as safe as possible

    :param loc: location of the existing lamps
    :param k: the amount of lamps you are allowed to add
    :return: minimal possible distance between the farthest lamps
    """
    pass
