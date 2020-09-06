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
import numpy as np


def poster_solution(heights: List[float]) -> float:
    """ Finds the biggest possible poster area

    :param heights: the height of every building, according to their position
    :return: the biggest possible poster area
    """

    """
    idea:
    most naive solution will be to check every possible set of buildings - and it takes O(n^3) time - not implemented.
    
    A better approach will be based on the idea of divide and conquer. we can notice than given a set of buildings, the
    width of the poster will be the amount of buildings, and the height will be the minimal of the buildings' heights.
    so, we know that if the building with the minimal height is in position i, then the maximal area is one of:
    1. the minimal height times the total amount of buildings
    2. the biggest area that can be achieved from buildings 0,...,i-1
    3. the biggest area that can be achieved from buildings i+1,...,n-1
    using this method we create a solution in an O(nlogn) runtime, implemented below.
    
    yet, this solution will not be enough for our last tests, and we would like to find linear-time solution. our
    solution will be based over dynamic programming.
    as we saw before, the height of the optimal poster will be the height of the shortest building within the chosen
    building set. we can change the way we look over this observation: we can find, for every building, the max set of
    buildings containing it with it as the shortest building, and find the poster area over those buildings. our output
    should be the maximum value of all of these areas.
    so, we would like to find, for every building, the largest consecutive set of buildings containing it such that it's
    the shortest building in the set. it can be done by finding the first building on it's left that is shorter than
    our building, and the same to the right, and use the group in between those buildings. the search for 'the first
    building on -some side- that is shorter than specific building can be performed dynamically to all buildings at 
    once.
    how can we do it in linear time?
    1. we initialize an empty stack.
    2. we iterate our buildings from left to right, every iteration would like to push a new building to the stack.
    3. the stack will maintain an important invariant: every value in the stack is larger than all the values below it.
    it means that we will indeed push the new building into the stack, only if it's height is bigger that the building
    currently at the top of the stack. if it's bigger, we keep popping building out of the top until the new building
    will be bigger than the building in the top, and then we push it.
    4. if there are no new buildings, we just pop all the stack out.
    
    now, let's assume we just pushed a building x into the stack, as long as we get buildings higher than x, it is
    assured that x will remain in the stack. but what will happen when we encounter the first building on the right that
    is smaller than x? note that all the current buildings above x must be higher than x, so the new building will be
    shorter from them as well. so, we will pop all buildings above x and x itself. it means that we will pop a building
    out of the stack only when the currently tested building is the first one on ot's right that's shorter that it!
    what about the left side?
    notice that when we pushed x into the stack, we popped all buildings the x is shorter from. it means that the
    building just below x in the stack will be the first on it's left that x is not shorter from! with this observation,
    we can find for every building the maximal set of groups where it's the shortest one, and get the maximal poster
    area out of these possibilities.
    """

    # #  divide and conquer approach:
    # def max_poster_area(heights):
    #     if len(heights) == 0:
    #         return 0
    #     else:
    #         min_idx = np.argmin(heights)
    #         return np.max([max_poster_area(heights[:min_idx]),
    #                        max_poster_area(heights[min_idx + 1:]),
    #                        len(heights) * heights[min_idx]])
    #
    # return max_poster_area(heights)

    #  dynamic programming approach
    stack = []
    max_area = 0
    n = len(heights)
    for i in range(n):

        if not stack or heights[stack[-1]] <= heights[i]:
            stack.append(i)

        else:
            while stack and heights[stack[-1]] > heights[i]:
                popped_idx = stack.pop()
                width = i - (stack[-1] + 1) if stack else i
                max_area = max(max_area, heights[popped_idx] * width)
            stack.append(i)

    while stack:
        popped_idx = stack.pop()
        width = n - (stack[-1] + 1) if stack else n
        max_area = max(max_area, heights[popped_idx] * width)

    return max_area
