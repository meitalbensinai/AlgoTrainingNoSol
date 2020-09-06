"""
problem formalization:

you are given an unweighted directed graph with N nodes, numbered from 0 N-1. In addition you are given 2 nodes, source
and target. If a path from source to target exists, return 0. else, return the minimal amount of edges that flipping
them will create a path from source to target. if it's not possible, return -1.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: shown in graph.jpg, source: 0, target: 6
output: 2

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 10 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 10 test:
- tests 1-7 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 8-10 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

import networkx as nx
import os


def reverse_edges_solution(path_to_graph: str, source: int, target: int) -> int:
    """ Finds the minimal amount of edges that has to be reversed in order to create a path from source to target

    :param path_to_graph: path to the pickle file with the graph input
    :param source: the number od the wanted source
    :param target: the number od the wanted target
    :return: minimal amount of edges to reverse
    """
    g = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))
    pass
