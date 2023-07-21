[Lecture Notes](http://cs229.stanford.edu/notes2020spring/cs229-notes2.pdf)

## Generative Learning Algorithms

Generative learning algorithms are a class of machine learning algorithms that aim to understand and model the underlying probability distribution of the input data. These algorithms learn the characteristics and patterns of the training data to generate new samples that are similar to the training examples.

The key idea behind generative learning is to build a model of the data that captures its statistical properties. Once the model is trained, it can be used to generate new data points that resemble the original training data.

Generative learning algorithms can be categorized into two main types: generative models and generative adversarial networks (GANs).

The example given in the lecture is using the Gaussian distribution on two parameters. 

## Gaussian Discriminant Analysis
[GeeksForGeeks Tutorial](https://www.geeksforgeeks.org/gaussian-discriminant-analysis/)

Gaussian Discriminant Analysis (GDA) is a generative learning algorithm used for classification tasks. It assumes that the input features follow a Gaussian distribution and estimates the parameters of these distributions to make predictions.

A brief explanation of the Gaussian Discriminant Analysis algorithm:

1. Input data: GDA takes a set of input samples, where each sample is described by a set of features. These features are assumed to be continuous and follow a Gaussian (normal) distribution.

2. Model initialization: GDA initializes the parameters of the Gaussian distributions for each class. This includes the mean vector and the covariance matrix for each class.

3. Estimating parameters: The algorithm estimates the parameters (mean and covariance) for each class by calculating the sample mean and covariance from the training data belonging to that class.

4. Computing class probabilities: Given the estimated parameters, GDA calculates the class probabilities using Bayes' theorem. It calculates the prior probability of each class based on the training data and computes the likelihood of the input belonging to each class based on the estimated Gaussian distributions.

5. Prediction: To make predictions, GDA selects the class with the highest posterior probability as the predicted output. This is achieved by comparing the class probabilities obtained in the previous step.


Gaussian Discriminant Analysis assumes that the covariance matrices of all classes are equal (known as homoscedasticity). However, if the covariance matrices are different (known as heteroscedasticity), the algorithm becomes Quadratic Discriminant Analysis (QDA), which estimates a separate covariance matrix for each class.

GDA is a simple and computationally efficient algorithm that works well when the assumption of Gaussian distribution holds true.

## Generative vs Discriminative Learning Algorithms

Generative and discriminative learning algorithms are two different approaches in machine learning that tackle the problem of classification in distinct ways.

**Generative Learning Algorithms:** Generative learning algorithms aim to model the underlying probability distribution of the input data. By learning the joint probability distribution of the input features and the corresponding class labels, generative models can generate new samples and perform various tasks beyond classification. 

**Discriminative Learning Algorithms:** Discriminative learning algorithms, on the other hand, focus solely on modeling the decision boundary between different classes. Instead of modeling the entire probability distribution, discriminative models directly learn the mapping from input features to class labels.

## Naive Bayes

Naive Bayes is a popular classification algorithm based on Bayes' theorem, a fundamental concept in probability theory. It is called "naive" because it makes a strong assumption of feature independence, meaning that it assumes the features are conditionally independent of each other given the class label. Despite this simplifying assumption, Naive Bayes often performs well and is widely used in text classification, spam filtering, and other tasks.

The example given in the lecture is for filtering spam. The naive approach here means that weather a word is found in a spam email or not, doesn't make it any different. The words in the model stay the same. 