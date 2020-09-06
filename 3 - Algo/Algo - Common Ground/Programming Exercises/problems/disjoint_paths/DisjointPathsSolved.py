"""
problem formalization:

you are given a directed connected graph with N nodes numbered from 0 to N-1. in addition you are given two nodes,
source and target.
As you know, there can be many different paths from source to target. count the maximal amount of such paths such that
every pair of paths is edge disjoint (the paths doesn't share any edge).

Create an EFFICIENT algorithm to perform the given task.

--before you proceed, READ the next mathematical section!--

-----------------------------------------------------------------------------------------------------------------------

Mathematical Section:  (shall be given as a hint if necessary)

1. Integrality theorem:
max-flow is tha maximal value of total flow that can reach the target node. knowing the value of the max-flow tells us
nothing about the flow on every edge, and there might be configurations of flows that obtain the max-flow to target.
yet, when the capacities over every edge are integers, the integrality theorem tells us that one configuration exists
that obtains the max-flow, and in addition the flow over every edge is an integer!
you might find the property useful for the given exercise.

2. Why does this exercise useful?
when we look at communication networks, we want to be able to deal with failures in some parts of the networks.
So, for such network, we will like to know the maximal number K such that even is we choose randomly K edges from the
network and disconnect them, there still exists at least one path from source to target (this is mathematically called
min-cut). Menger's theorem. using the max-flow-min-cut theorem (you're welcome to read online) shows that K is also
equal to the number of disjoint paths you where asked to find.

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

    """
    idea:
    we will transfer the given graph into flow network, such that the capacity over every edge equals 1, and find the
    maximum flow. we can show that the maximum flow (M) equals to the amount of edge disjoint paths in the graph (A):
    
    A <= M:
    let's set the flow to be 1 over every edge if it's part of any of the paths, else 0. this satisfy the capacity
    constrain. this way, a unit of flow arrived the target through every such path, so the total flow is A.
    therefore, the maximum flow is at least A.
    
    M <= A:
    using the integrality theorem (see mathematical section above), there exist a flow over the edges that uses only
    integers. since our capacities are all ones, it means that the flow over every edge can be 0 or 1. it means there
    are at least M edges leaving the source, each one has flow of 1.
    now we use conservation:
    for each of these edges, let's look at it's end-vertex. it must have an out-going edge with flow 1 (by conservation)
    and it must be edge we haven't visited yet (to keep the capacity constrain). this way, for every edge with flow 1
    leaving source, we can create a new edge-disjoint path from source to target, so there are at least M such paths.
    
    so, A=M, and we should just find the maximal path.
    """

    g = nx.read_gpickle(os.path.join(os.getcwd(), path_to_graph))
    nx.set_edge_attributes(g, {edge: 1 for edge in g.edges}, 'capacity')
    return nx.maximum_flow_value(g, source, target)
