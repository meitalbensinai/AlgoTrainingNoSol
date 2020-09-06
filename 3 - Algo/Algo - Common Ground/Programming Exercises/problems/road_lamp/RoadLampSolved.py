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
import numpy as np


def road_lamp_solution(loc: List[int], k: int) -> int:
    """ Adds lamps to the road to make it as safe as possible

    :param loc: location of the existing lamps
    :param k: the amount of lamps you are allowed to add
    :return: minimal possible distance between the farthest lamps
    """

    """
    idea:
    there are several 'efficient' ways to solve the problem. choosing the best one must take into account the possible
    ranges of the input values.
    we will use two methods, one that can solve the problem in O(KlogN) runtime, and another method solving in O(NlogM)
    runtime, where M is the length of the road. we will rather use the first method when dealing with cases where N > K,
    and use the second method when dealing with cases where K > N
    
    method A - O(KlogN):
    we work greedy and add a lamp at a time.
    we will look at the N-1 section created by the initial N lamps - we know they are sorted by length. each section
    will have an effective length, which is initially the initial length. every time, we will add another lamp to the
    section with the current biggest effective length, and thus we will be able to split it once more. we now re-sort
    the section by effective length, but since it was pre-sorted and we only changed one value, it takes us O(logN)
    time. at the end we return the biggest effective length.
    
    method B - O(NlogM):
    we know that our final output is an integer in the range [1, M]. given a guess about the output, d, we can check if
    it's correct - for each of the N-1 initial sections, we find the needed amount of lamps in order to split it into
    sub-sections smaller than d, and sum over all the N-1 initial sections. if the total is smaller than K - we can
    achieve the result d, and if it's bigger that K - we cannot. in addition, notice that if for some d' in range [1, M]
    we succeed in this process, we will succeed in any attempt with d > d'. therefore we can deduce that this attempts
    will succeed for every d >= d_optimal and will fail for all d < d_optimal, where d_optimal is the desired output.
    every 'attempt' like this takes us O(N) time, and by binary searching in the range [1, M] we can find d_optimal
    in at most O(logM) attempts.
    """

    n = len(loc)
    length = np.array(loc[1:]) - np.array(loc[:-1])
    if n >= k:
        parts = np.ones(n-1)
        for _ in range(k):
            effective_length = length/parts
            parts[-1] += 1
            idx = np.searchsorted(effective_length[:-1], length[-1]/parts[-1])
            length[idx:] = np.roll(length[idx:], 1)
            parts[idx:] = np.roll(parts[idx:], 1)
        return np.ceil(length[-1]/parts[-1])

    else:
        minimal = 1
        maximal = loc[-1]
        while minimal != maximal:
            d = int((minimal + maximal)/2)
            total = 0
            for i in range(n-1):
                total += np.ceil(length[i]/d) - 1
            if total > k:
                minimal = d + 1
            else:
                maximal = d
        return maximal

