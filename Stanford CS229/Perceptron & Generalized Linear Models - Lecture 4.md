
## Perceptron

The perceptron algorithm is for adjusting for unclassified datasets. The formula for this algorithm is:
**Θj  =  Θj + α\*(yi -  h(x)i)\*xi**.
Here h(x) can be 0 or 1 (for g(z) values z < 0 -> 0, z >= 0  -> 1). This way we find all the unclassified or datasets that are incorrectly classified. Here yi can also be 0 or 1 so in most cases we can only get 0, 1, -1. This tells us how we should adjust our vector and in what direction.

## Exponential Family

Bernoulli (binary data), Gaussian (for real data), Poisson (positive numbers) are all part of the Exponential family. They all can be represented by the formula for the exponential family which is:

![[b0fe1a16a55ec44ac2728f28a48562ab674e0d15.svg]]

## Generalized Linear Models  (GLMs)

For GLMs there is a set of rules/assumptions that have to be followed for the algorithm to be a GLM.

1. y | x, Θ - is part of the exponential family
2. **η** - R^(n)
3. Test time E\[y\[x,Θ]] - estimation

## Softmax Regression

Softmax regression, also known as multinomial logistic regression, is a supervised learning algorithm used for classification tasks where the output variable can take on multiple classes. It is an extension of the logistic regression algorithm, which is designed for binary classification.

The goal of softmax regression is to assign probabilities to each class label based on the input features. It calculates the probability of an input belonging to each class and selects the class with the highest probability as the predicted output.

