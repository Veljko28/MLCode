

## K-mean clustering

K-means clustering is a popular unsupervised machine learning algorithm used to partition a given dataset into distinct groups or clusters based on similarity or proximity of data points. It aims to assign each data point to the cluster that has the closest mean or centroid.

Here's how the K-means clustering algorithm works:

1. Initialization: Choose the number of clusters K that you want to create. Randomly initialize K cluster centroids within the feature space.

2. Assignment: Assign each data point to the cluster whose centroid is closest in terms of Euclidean distance or other distance measures. This is done by calculating the distance between each data point and the centroids and assigning it to the nearest centroid.

3. Update centroids: After assigning all data points to clusters, compute the new centroids by taking the mean of all the data points assigned to each cluster. This step updates the cluster centroids.

4. Repeat steps 2 and 3: Iteratively repeat steps 2 and 3 until convergence criteria are met. The convergence criteria can be a maximum number of iterations, minimal change in cluster assignments, or reaching a predefined level of accuracy.

5. Final clustering: Once the algorithm converges, the final cluster assignments are obtained. Each data point belongs to the cluster associated with the nearest centroid.


K-means clustering aims to minimize the within-cluster sum of squared distances, also known as inertia or distortion. It seeks to create compact and well-separated clusters based on the proximity of data points to their respective centroids.

![[kmeans.gif]]

## Density Estimation

Density estimation is a fundamental task in statistics and machine learning that involves estimating the underlying probability density function (PDF) of a dataset. It aims to understand the distribution of data points and capture the underlying patterns or structure within the data.

Density estimation can be approached using various techniques, including parametric and non-parametric methods:

Parametric methods: Parametric density estimation assumes a specific functional form for the PDF and estimates the parameters of that distribution. Common parametric approaches include Gaussian (Normal) distribution, exponential distribution, or mixture models. These methods work well when the data distribution aligns with the assumed parametric form.


## Mixture of Gaussian

A mixture of Gaussian (MoG), also known as Gaussian mixture model (GMM), is a probabilistic model that represents a dataset as a combination of multiple Gaussian distributions. It is widely used for density estimation and clustering tasks, where the data is assumed to be generated from a mixture of underlying Gaussian distributions.

In a mixture of Gaussian model:

1. Components: The model assumes that the data points are generated from a finite number of Gaussian components, each characterized by its mean, covariance, and weight. The weight represents the probability of selecting a specific component.

2. Probability density function: The probability density function of a mixture of Gaussian model is the weighted sum of the individual Gaussian component probability density functions. Each component contributes to the overall density based on its weight.

3. Model parameters: The parameters of a mixture of Gaussian model include the means, covariances, and weights of the Gaussian components. These parameters are typically estimated using techniques such as the Expectation-Maximization (EM) algorithm or maximum likelihood estimation.

## EM (Expectation-maximization algorithm)

The Expectation-Maximization (EM) algorithm is an iterative optimization algorithm used to estimate the parameters of statistical models, particularly in cases involving missing or incomplete data. It is commonly employed in machine learning and statistics to estimate parameters for models such as Gaussian mixture models (GMMs) or hidden Markov models (HMMs).

The EM algorithm consists of two main steps: the expectation step (E-step) and the maximization step (M-step). It iteratively alternates between these steps until convergence is reached.

1. Expectation step (E-step): In the E-step, the algorithm computes the expected values of the unobserved or missing variables, given the current estimates of the model parameters. It calculates the posterior probabilities or "responsibilities" of each data point belonging to each component of the model.

2. Maximization step (M-step): In the M-step, the algorithm updates the estimates of the model parameters based on the computed expected values from the E-step. It maximizes the likelihood of the observed data by adjusting the model parameters, typically using techniques like maximum likelihood estimation or maximum a posteriori estimation.

3. Iterative process: The E-step and M-step are repeated iteratively until the algorithm converges. Convergence is typically determined by a change in the log-likelihood or the parameters reaching a threshold.

EM algorithm in Gaussian Mixture Models (GMMs): In the context of GMMs, the EM algorithm estimates the parameters of the mixture components (e.g., means, covariances, and weights) using the observed data. In the E-step, it computes the posterior probabilities of each data point belonging to each component, based on the current estimates of the parameters. In the M-step, it updates the parameters by re-estimating the means, covariances, and weights based on the computed responsibilities.

![[EM_Clustering_of_Old_Faithful_data.gif]]

## Jensen's inequality

Jensen's inequality is a fundamental result in mathematical analysis that relates the convexity or concavity of a function to the expectation of that function. It provides a powerful tool for reasoning about the relationships between functions and their expected values.

Mathematically, Jensen's inequality states the following:

Let f(x) be a convex function (or concave function) defined on an interval I, and let X be a random variable taking values in I. If E\[X] denotes the expectation (average) of X, then:

For a convex function: E\[f(X)] ≥ f(E\[X])

For a concave function: E\[f(X)] ≤ f(E\[X])

In simpler terms, for a convex function, the expected value of the function applied to a random variable is greater than or equal to the function applied to the expected value of the random variable. Conversely, for a concave function, the expected value of the function is less than or equal to the function applied to the expected value.