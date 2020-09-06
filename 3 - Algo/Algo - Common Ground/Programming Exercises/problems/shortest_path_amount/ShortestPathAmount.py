"""
problem formalization:

you are given an unweighted (directed or undirected) graph with N nodes, numbered from 0 to N-1. In addition you are
given number between 0 to N-1 representing one of the nodes (source). Compute, for every node in the graph, the amount
of different paths from the source to the node that are shortest.
note that the amount of paths from the source to itself is 1 (the empty route).

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: shown in graph.jpg, source: 0
output: [1, 1, 1, 2, 2, 2, 4]

(the paths to node 6:
0 -> 1 -> 3 -> 4 -> 6
0 -> 1 -> 3 -> 5 -> 6
0 -> 2 -> 3 -> 4 -> 6
0 -> 2 -> 3 -> 5 -> 6)

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 4.5 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 10 test:
- tests 1-5 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 6-10 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List
import networkx as nx
import os


def shortest_path_amount_solution(path_to_graph: str, source: int) -> List[int]:
    """ Finds for each node the amount of different possible paths from source to it that are shortest

    :param path_to_graph: path to the pickle file with the graph input
    :param source: the number of the wanted source
    :return: array with the amount of shortest paths
    """
    g = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))
    pass
