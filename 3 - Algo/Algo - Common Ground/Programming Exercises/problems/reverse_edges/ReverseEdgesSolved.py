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

    """
    idea:
    we create a duplicate graph of the original, d.
    d will be a directed graph with the same nodes as g. every edge in g will appear in d as two edges:
    1. the original node will have a zero weight.
    2. the reversed of the original node will have weight 1.
    
    now we run dijkstra from source to target. since all the original nodes have 0 weight, we can use them without
    carrying any cost. every time we choose to reverse an edge, we pay for that with 1 unit of cost. so - the total
    cost of the path will be the minimal amount of edges needed to be reversed.
    """

    g = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))
    d = nx.DiGraph()
    d.add_nodes_from(g.nodes)

    # we loop the edges twice, first adding the reversed ones. this way, if both directions appear in graph, they will
    # be changed in the second loop and be set with weight 0 and not 1.
    for u, v in list(g.edges):
        d.add_weighted_edges_from([(v, u, 1)])

    for u, v in list(g.edges):
        d.add_weighted_edges_from([(u, v, 0)])

    try:
        amount = nx.single_source_dijkstra(d, source, target)[0]
    except nx.NetworkXNoPath:
        amount = -1
    return amount
