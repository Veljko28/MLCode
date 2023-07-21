
## Variance and bias from ideal

In the context of estimating the error of a machine learning model, the terms variance and bias refer to two different sources of error that contribute to the gap between the model's performance and the ideal or optimal error.

1. Bias refers to the error introduced by approximating a real-world problem with a simplified model. It captures the model's tendency to consistently deviate from the true values or the underlying pattern. A high bias implies that the model is unable to capture the complexity of the data and makes overly simplistic assumptions.
2. Variance refers to the error caused by the model's sensitivity to fluctuations or noise in the training data. It measures how much the predictions of the model vary when trained on different subsets of the data.

## Risk Error

Risk error, also known as generalization error, is a term used in machine learning to refer to the expected error or performance of a trained model on unseen data. It represents the model's ability to generalize its learned patterns from the training data to new, unseen instances.

The risk error can be decomposed into two components: the approximation error and the estimation error.

## Empirical Error

Empirical error, also known as training error or empirical risk, refers to the error or loss incurred by a machine learning model on the training dataset. It represents the discrepancy between the model's predictions and the true target values observed in the training data.

## Bayes Error

Bayes error, also known as the Bayes risk or irreducible error, is the minimum possible error rate that can be achieved on a given machine learning problem, assuming perfect knowledge of the true underlying data distribution.

In other words, the Bayes error represents the lowest possible error rate achievable by any model, regardless of its complexity or algorithm. It serves as a theoretical lower bound on the performance that can be attained.

## Approximation Error

The approximation error, also known as the bias error, represents the error introduced by using a simplified model or making assumptions that deviate from the true underlying patterns in the data. It quantifies the model's inability to represent the true relationship accurately. Models with high approximation error tend to underfit the training data and have limited expressive power.

## Estimation Error

The estimation error, also known as the variance error, captures the error introduced by the finite size of the training dataset and the randomness inherent in the learning process. It measures how much the model's predictions vary when trained on different subsets of the data. Models with high estimation error tend to overfit the training data and have excessive sensitivity to the specific samples in the training set.

**The empirical error is a measure of how well the model fits the training data.**

## Empirical Risk Minimization (ERM)

**Empirical Risk Minimization (ERM)** is a principle and approach commonly used in machine learning to train models based on minimizing the empirical risk or training error. ERM involves finding model parameters that yield the lowest possible error on the training data.

The ERM principle assumes that the training data is representative of the underlying data distribution and that minimizing the empirical risk will lead to good generalization. However, it is essential to be mindful of potential pitfalls such as overfitting, where the model performs well on the training data but poorly on unseen data.