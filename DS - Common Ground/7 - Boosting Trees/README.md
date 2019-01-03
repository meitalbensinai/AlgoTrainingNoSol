Read sections 10.1-10.5 of ESL (pages 337-346) about AdaBoost.

Explain to yourself the following, then discuss with your supervisor.

1. How does AdaBoost operate? What happens in every stage?

2. How are the weights updated in AdaBoost Simplify and explain qualitatively.

3. What is the loss function underlying AdaBoost? What relaxation is done in optimizing it?

4. Does it make sense to continue training AdaBoost after the accuracy has stabilized? Why?

5. What is the statistical quantity that the output of AdaBoost approximates? In what sense is the exponential loss equivalent to cross entropy? We will next discuss how they differ.

Read section 10.6.

6. Replicate figure 10.4

7. Suppose you perform binary classification on a dataset where some of the labels are wrong. Which of cross-entropy and exponential loss is more suitable? Why?

Read the “meta” 10.7. Pay attention to table 10.1.

Gradient Boosting is considered to be one of the most powerful learning algorithms, but its details are tough. The team only knows little about it; Your mission is to make an end to this state!

Read 10.9-10.13, up to page 370.

8. Research the different flavors of gradient boosting libraries, such as xg-boost, catboost and the sklearn build in classifier. Run the algorithm on an interesting dataset of your choice with all frameworks and compare the results with other classifiers.

9. Present the work to the whole team and explain the differences between the various frameworks. Emphasize the practical aspects: which library to use, and how to do it. How to tune the parameters accordingly. Make your presentation clear: communicating results effectively is just as important as obtaining them.

Good luck!
