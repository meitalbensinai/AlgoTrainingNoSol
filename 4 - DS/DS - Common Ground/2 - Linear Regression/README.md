# Linear Regression

Read chapter 3 in Bishop up to p.152. 

Explain to yourself and to your supervisor the following:

1. What is the advantage of using sequential learning for fitting linear model over the analytical solution?

2. What is the geometrical meaning of the least square solution to linear regression?

3. Why does L1 regularization tend to make coefficients vanish exactly, while L2 doesn’t?

4. What is the bias-variance tradeoff?

Use sklearn.dataset.load_boston to load boston dataset.

Then finish the next exercise:

Use sklearn.datasets.load_boston to load the boston dataset. It contains a description of the data.

1.	Fit a linear regression model with medv as the response and lstat as the predictor. Do this in 3 ways:

    Analytically, Sequential Learning, Sklearn's build in predictor.
    
    Compare the resulting lines.

2.	Plot the data along the fitted line. What does the model predict for lstat=10?

3.	Fit a linear regression model using lstat and a new feature that is equal to two times lstat. What happened?

4.	Fit a linear regression model using all features except age. Did your prediction become better?

5.	Using linear regression, compte a parabolic least-squares fit for the target variable using only lstat. Plot your result. Did this improve upon your fit from 1a?

6.	Investigate what happens when plotting a polynomial regression of higher order with regularization. Use both L1 and L2 and plot the qualitive behaviour of the coefficients in each case. What combination would you choose for your final model?
