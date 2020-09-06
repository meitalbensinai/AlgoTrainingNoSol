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
- tests 1-3 are visible to you, and you can access thr input using 'get_input' method from utils.Test.
- tests 4-7 are not visible to you, and need to pass them without knowing the input.
It is assured to you that all input is legal and fits the solution signature.

-----------------------------------------------------------------------------------------------------------------------

Documentation:

After passing all tests, write a doc in Confluence describing your solution.
In the doc, analyze the runtime of the algorithm you used.

"""

from typing import List
import networkx as nx
import numpy as np
import os


def articulation_points_solution(path_to_graph: str) -> List[bool]:
    """ Check for every node if it's an articulation point

    :param path_to_graph: path to the pickle file with the graph input
    :return: mask representing for every node if it's an articulation point or not
    """

    """
    idea:
    the naive solution will be to remove different vertex every time and then traverse the graph to check amount of
    connected components. this will take O(V(V+E)) time.
    we can solve the problem dynamically in O(V+E) time by using the concept of back edge (can be given as a hint).
    let's look at the DFS tree created by traversing from random source.
    
    when we look at some vertex u in the graph, it will exist somewhere in the tree. to make sure u is not an
    articulation point, we need no make sure that any of its descendants in the tree can be connected somehow else to
    the rest of the tree. this connection is called a back-edge.
    from the nature of DFS algorithm, we know that for a given vertex, each one of it's neighbors must be:
    1. not discovered yet, therefore within the subtree below it.
    2. already discovered, and therefore the edge connecting them will not be part of the tree. these edges are called
    back-edges, and they allow us to get back from the subtree into the tree even without the removed vertex.
    therefore, in order to say that some vertex u is not an articulation point, we want to make sure that every node in
    it's subtree has a back-edge to a node discovered before u, or that one of it's descendants had such back-edge.
    
    therefore, we will hold 2 properties for every node u in the tree/graph:
    1. time[u] will be the discovery time of u in the traversal.
    2. low[u] will be the the lowest discovery time of node reachable from u by a back-edge, or reachable by one of its
    descendants by a back-edge. this array can be built dynamically in O(V+E) time.
    
    now with 2 arrays, we can make the decision about articulation points more easily: a node u is an articulation point
    if for one of it's direct children u, low[u] >= time[v] holds - this exactly means that one of its descendants
    cannot connect to the rest of the tree. checking this conditions takes total runtime of O(E).
    
    the only exception is the source, because it's the first discovered one, so for all vertex u exists
    low[u] >= time[s], and that does not mean it's an articulation points.
    but, we can notice that when we start building the tree, we choose one of it's children and start traversing from
    it. if source has another child, it means that the second child wasn't reachable from the first child, but only
    through the source. therefore, the source is an articulation point iff it has more than one child.
    """

    g = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))
    t: nx.DiGraph = nx.dfs_tree(g, source=0)
    n = len(g.nodes)

    time = np.zeros(n)
    for i, node in enumerate(nx.dfs_preorder_nodes(g, source=0)):
        time[node] = i

    low = time.copy()
    for node in nx.dfs_postorder_nodes(g, source=0):
        low[node] = np.min([time[node]] + [low[v] for v in g.neighbors(node) if v not in t.predecessors(node)])

    articulation_points = np.tile(False, n)

    articulation_points[0] = len(list(t.successors(0))) > 1
    for node in range(1, n):
        articulation_points[node] = np.any([low[v] >= time[node] for v in t.successors(node)])

    return list(articulation_points)
