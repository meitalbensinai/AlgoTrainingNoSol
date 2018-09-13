Trees – use sklearn library

1.	Load and prepare the dataset for classification 

2.	Define a baseline

3.	Use cross validation with 10 k-folds to test the next classifiers, and calculate the accuracy for each one: 

•	Decision Tree Classifier https://www.kaggle.com/dmilla/introduction-to-decision-trees-titanic-dataset 

•	Random Forest Classifier https://www.kaggle.com/raviolli77/random-forest-in-python 

•	Gradient Boosting Classifier http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/ 

•	Adaptive Boosting Classifier (use your best Decision Tree model)

https://www.quora.com/What-is-the-difference-between-gradient-boosting-and-adaboost 

Notice the improvement in accuracy. Tune the parameters for each tree to find the most accurate configuration using GridSearchCV for max_depth, max_features, algorithms and learning rate (when needed of course).  Save the configurations for question 4.

4.	Create confusion matrix for each classifier
