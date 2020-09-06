"""
problem formalization:

you are given a tree with N nodes and N-1 edges. Nodes are numbered from 0 (root) to N-1.
You are allowed to 'rotate' the tree by defining any of it's nodes as the root.
We define the depth of the tree to be the length of the path from the root to the farthest leaf in the tree.
for every node, we define the depth of the node to be the depth of the tree rotated around this node as a root.

Count how many nodes has the same depth as the root.

Create an EFFICIENT algorithm to perform the given task.

-----------------------------------------------------------------------------------------------------------------------

Example:

input: shown in tree.jpg
output: 2

* The nodes with the depth of 3 (the depth of the root) are root itself and node 3.
* The process of rotation/root changing is shown in rotated_tree.jpg

-----------------------------------------------------------------------------------------------------------------------

Limitations:

time - 2 seconds

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


def rotations_solution(path_to_tree: str) -> int:
    """ Count how many nodes in the tree has the same depth as the root

    :param path_to_tree: path to the pickle file with the tree input
    :return: amount of node with the same depth as the root
    """

    t = nx.read_gpickle(os.path.join(os.getcwd(), path_to_tree))
    pass
