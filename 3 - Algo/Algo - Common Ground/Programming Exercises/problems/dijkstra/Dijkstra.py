"""
problem formalization:

implement dijkstra single-source-all-targets-shortest-path algorithm by yourself. (go for the naive implementation of
the priority queue or use libraries for better implementations from anaconda)

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

no Example this time.

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 0.1 seconds

-----------------------------------------------------------------------------------------------------------------------

Testing:

this time you will have only one test.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

no need for documentation for this task.

"""

from typing import List
import networkx as nx
import os


def dijkstra_solution(path_to_graph: str, source: int) -> List[float]:
    """ single-source-all-targets dijkstra

    :param path_to_graph: path to the pickle file with the graph input. node of the graph are numbered from 0 to N-1.
    the weight of every edge is given in the 'weight' attribute of the edges.
    :param source: desired source
    :return: List representing the shortest path length from source to each node.
    """
    g = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))
    pass
