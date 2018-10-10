# Linear Regression

Read pages 59-103 in ISLR book.

Then finish the next exercise:

Use sklearn.datasets.load_boston to load the boston dataset. It contains a description of the data.

Univariate regression

1.	Fit a linear regression model with medv as the response and lstat as the predictor.

2.	Plot the data along the fitted line

3.	What is the value of the R squared statistic in your model?

4.	What is the value of the F statistic?

5.	What does the model predict for the value lstat=10?

6.	Compute a 95% confidence interval associated with the value lstat=10.

Multivariate regression

1.	Fit a linear regression model using lstat and a new feature that is equal to two times lstat. What happened?

2.	Fir a linear regression model using all features except age. Did your prediction become better?

3.	Using linear regression, compte a parabolic least-squares fit for the target variable using only lstat. Plot your result. Did this improve upon your fit from 1a?

4.	Use p-values to find the highest exponent for which the polynomial regression fit keeps improving your model.
