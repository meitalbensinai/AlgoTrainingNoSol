1. Given the next table

| גשום | מעונן | קר |   |   |
|------|-------|----|---|---|
| כן   | כן    | כן |   |   |
| לא   | כן    | לא |   |   |
| לא   | לא    | לא |   |   |
| לא   | לא    | כן |   |   |
| כן   | כן    | לא |   |   |
| לא   | לא    | כן |   |   |
| לא   | כן    | לא |   |   |


a . Calculate support and confidence for the laws: Cloudy Dragging Rainy, Cloudy and Cold Dragging Rain

b. Manually run the a priori algorithm for min_support = 0.3 and min_confidence = 0.8. Specify the running of the algorithm.

2. Use the support function (df, rule) when:
a. df is a pandas data frame
b. rule is a string from the form x_1 and x_2 ... and x_k → x_ (k + 1) where all x_i is the name of a column in the data frame.
c. The function returns the support of the rule in df.

3.Realize functions with a signature similar to question 2 for confidence and lift.

4. We noted (with examples) major problems of the various measures for evaluating laws.

5. How many possible rules exist for information with n features when each feature has m values?

6. This question attempts to demonstrate that high confidence does not necessarily mean that the law that is returned is indeed a muscle in reality (ie, looking at high confidence is not important only to find significant laws that exist but to sift out laws that stem from mere randomness):

Suppose that our information has m completely random features (noise). Show that for m large enough almost certainly will have a law with confidence 1.
