"""
problem formalization:

A node in a connected undirected graph is called an 'Articulation point' (or cut-vertex) if removing it (and all of it's
edges) will separate the original graph into 2 different connected components. Find all the articulation points in the
given graph.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: shown in graph.jpg
output: [False, False, True, False, False]

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 0.35 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

After implementing your solution, test it with our given input by 'CheckSolution' file.
You have a total of 7 test:
- tests 1-3 are visible to you, and you can access the input using 'get_input' method from utils.Test.
- tests 4-7 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List
import networkx as nx
import os


def articulation_points_solution(path_to_graph: str) -> List[bool]:
    """ Check for every node if it's an articulation point

    :param path_to_graph: path to the pickle file with the graph input
    :return: mask representing for every node if it's an articulation point or not
    """
    g = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))
    pass
