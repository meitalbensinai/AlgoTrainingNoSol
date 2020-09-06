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
import numpy as np
import os


def dijkstra_solution(path_to_graph: str, source: int) -> List[float]:
    """ single-source-all-targets dijkstra

    :param path_to_graph: path to the pickle file with the graph input. node of the graph are numbered from 0 to N-1.
    the weight of every edge is given in the 'weight' attribute of the edges.
    :param source: desired source
    :return: List representing the shortest path length from source to each node.
    """
    g: nx.DiGraph() = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))

    n = len(g.nodes)
    weights = nx.get_edge_attributes(g, 'weight')

    # Initialization
    dist = np.tile(np.inf, n)
    dist[source] = 0

    q = dist.copy()
    for i in range(n):
        u = np.argmin(q)
        q[u] = np.inf
        for v in g.successors(u):
            if dist[v] > dist[u] + weights[(u, v)]:
                dist[v] = dist[u] + weights[(u, v)]
                q[v] = dist[v]

    return list(dist)
