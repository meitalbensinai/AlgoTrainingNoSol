# SVM

Read about SVM from ISLR pages 337-359

Answer questions 3,6 in exercise section

Then proceed with the next question:

In the next exercises assume the data is 2 dimensional and distributes uniformly on [0,1] X [0,1] unless otherwise stated.

# Part 1

In this exercise we assume the hypothesis we want to learn is classification by y=1-x:

Class = 1 if y>1- x1 -x2, otherwise 0

Create a train dataset by generating 1000 labeled points

Create a test dataset by generating 1000 unlabeled points

Classify each point according to a different kernel 

Show them on the same plot (one for every kernel). Correctly classified points in blue, misclassified in red. Try at least 3 different kernels which you see fit. Also plot the separating line.

What is the difference in total train and test time between different kernels?

Choose the appropriate kernel and use it in the next parts:

# Part 2

Extend the hypothesis for higher dimensions keeping the training and test sets balanced. Think what "extension of the hypothesis" means. Classify each point according to your chosen kernel. How are the training and test times depend upon the dimension? (what is the relation)

# Part 3

Denote the number of train samples N, and the dimension P. Test samples number is fixed. For every region N<<P, N=P, N>>P show the test error. Plot all results one informative graph. 

# Part 4

Repeat the exercise 1 with hypothesis of circle locates at (0.5,0.5) with radius of size 0.25. No need to plot separating line.


