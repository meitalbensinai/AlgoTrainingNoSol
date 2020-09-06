"""
problem formalization:

you are given a directed connected graph with N nodes numbered from 0 to N-1. in addition you are given two nodes,
source and target.
As you know, there can be many different paths from source to target. count the maximal amount of such paths such that
every pair of paths is edge disjoint (the paths doesn't share any edge).

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: shown in graph.jpg
output: 3

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 3.5 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 5 test:
- tests 1-3 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 4-5 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

import networkx as nx
import os


def disjoint_paths_solution(path_to_graph: str, source: int, target: int) -> int:
    """ Find the maximum amount of edge disjoint paths in graph from source to target

    :param path_to_graph: path to the pickle file with the graph input
    :param source: the desired source
    :param target: the desired target
    :return: maximum amount of disjoint paths
    """
    g = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))
    pass
