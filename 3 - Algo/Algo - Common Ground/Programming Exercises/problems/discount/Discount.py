"""
problem formalization:

you are trying to reach target from source, using some road system represented as directed graph. every road in this
system has a toll that has to be paid for using it. The company in charge of the toll values is now giving a special
discount - "for every trip on our roads, you get a discount for the next trip! the discount value equals to the toll
of the road with the highest toll you have been using!"
you currently have k dollars to use. you actually don't care to spend money now, and you are willing to drive in any
path from source to target as long as its total cost doesn't exceed k. yet, you know that tomorrow your son will be
using this road system, and you want to give him the highest discount you can achieve.
(Note - even if it means that you need to pay now more money that the discount will save you, find the biggest possible
discount. you didn't wake up in rational mood today..)
Find the biggest discount you can achieve for your son, without paying more than k dollars yourself.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: roads and tolls shown in graph.jpg, source: 0, target: 3, k: 10
output: 8

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 3.5 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 7 test:
- tests 1-4 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 5-7 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

import networkx as nx
import os


def discount_solution(path_to_graph: str, source: int, target: int, k: int) -> int:
    """ Finds the biggest discount that can be achieved

    :param path_to_graph: path to the road graph. tolls are edge-attributed under 'weight' label.
    :param source: the desired source
    :param target: the desired target
    :param k: your maximal money bound
    :return: value of the biggest discount.
    """
    g = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))
    pass
