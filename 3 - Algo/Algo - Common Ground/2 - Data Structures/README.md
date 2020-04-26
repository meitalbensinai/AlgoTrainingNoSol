# Data Structures

Part 1: Asymtotic notations, Arrays and Sorting (if you fell you already know the material, only skim through it)

A. Read about asymptotic notations in IA p.43-49 (Only if your'e not familiar with the idea!)
B. Read about arrays and insertion sorting in AI p.16-29
C. Read abount Divide-and-Conquer methods and merge sorting in AI p.29-37


Part 2: Basic Data Structures

A. Read introduction in IA p.229-231
B. Read about the next data structures and do the given exercises:
	1. Stack/Queue - IA p. 232-253. Answer question 10.1-6 in p.236
	2. Linked list - IA p. 236-240. Answer question 10.2-7 in p.241
	3. Binary search tree - IA p. 286-298. Answer question 12-1 in p.303
	4. Heap (and heap sort and priority queue) - IA p. 151-166. Answer question 6-3 subsections c-f.
	5. Hash table - IA p.253-264. Answer question 11.2-6
C. Create a table sowing the running time (average and best) for SEARCH, INSERT, DELETE for every data structure above (skip heaps).
D. Implement the data data structures you compared. Perform SEARCH, INSERT and DELETE on every one of them (with diffenet input sizes)
to empiricaly prove the running times you found. Also, find inputs that get the worst running time for each of the datastructures.
As for heap, implement heap and use to perform a heapsort. Implement merge sort and one of insertion/selection sort and compare the 3
sorting algorithms on different sized inputs.


Part 3: Advanced Data Structures

You are given two problems that have difficulties with the basic data structures you just read about.
For every problem, read online and find a better data structure to deal with the problem. Read about the data struture and find out the running time
of the main operations that can be performed on it. If there are several fitting data structures in yout opinion, compare them.

1. You are holding a dataset containing 10^17 keys (there is no space problem).
You want to be able to perform SEARCH, INSERT and DELETE operations on the data.
Notice that the app you develop will be used in real-time operational situations, and if any of the operation takes too long - life may be in risk..

2. You are currently working for WAZE and help them improve the app. The upcoming new feature you develop will help user to find the
closest gas station to their current location.
You have a data about the locations of all the gas service stations over a 2D map. what is the best data dtucture to store them?