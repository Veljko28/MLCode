
## EM convergence 

EM convergence refers to the condition where the Expectation-Maximization (EM) algorithm has reached a stable and optimal solution. In other words, the EM algorithm has iteratively updated the model parameters until they no longer significantly change with further iterations.

At convergence, the algorithm has effectively estimated the parameters, and further iterations are not necessary as they will not lead to significant improvement.
Convergence is typically checked by monitoring the change in the log-likelihood or the model parameters between iterations.  

## Factor Analysis model 

The factor analysis model assumes that the observed variables are linear combinations of a few underlying latent factors and some unique (error) terms. The goal is to estimate the factors and their loadings on the observed variables, which represent the strength of the relationship between the factors and the variables.

Mathematically, the factor analysis model can be expressed as follows:

X = LF + ε

- X is a matrix of observed variables (data matrix).
- L is a matrix of factor loadings, indicating the relationships between the factors and the observed variables.
- F is a matrix of latent factors, representing the unobserved underlying variables that influence the observed variables.
- ε is a matrix of unique (error) terms, capturing the variance in the observed variables not explained by the factors.

## Probability Density Function (PDF)

A fundamental concept in probability theory and statistics used to describe the probability distribution of a continuous random variable.

In simple terms, a probability density function represents how likely a continuous random variable is to take on specific values within a certain range. Unlike discrete random variables, which have probability mass functions (PMFs) that assign probabilities to individual values, continuous random variables have probability density functions that describe the likelihood of a range of values.

The PDF of a continuous random variable f(x) is a non-negative function defined over the entire real line, satisfying the following properties:

1. Non-negativity: f(x) ≥ 0 for all x.

2. Area under the curve: The total area under the PDF curve must be equal to 1, representing the certainty that the random variable falls within its entire range.


The probability that a continuous random variable X falls within a specific interval \[a, b] can be calculated by integrating the PDF over that interval:

P(a ≤ X ≤ b) = ∫\[a to b] f(x) dx