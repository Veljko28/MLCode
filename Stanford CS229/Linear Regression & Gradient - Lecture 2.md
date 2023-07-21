
**Linear Regression** is the simplest example of supervised learning.

In **Gradient Descent** we are trying to find the local minimum of the parameter **Θ (Theta)**. To do this we take the partial derivative of the function J(Θ). We adjust the learning rate which is defined as alpha (**α**).  
  
**J(Θ)** is a function that represents the sum of all the error margins squared. The formula for J(Θ) is  
J(Θ) = Sum of (from i to n) (h(x\[i])   - y\[i])^2  
  
This type of gradient descent is called batch gradient descent. If you had a dataset of 10 million items every time you needed to update an item in your dataset, you would need to calculate the value of J again which would take a long time.  
  
To fix this we use **Stochastic gradient descent** doesn't update the whole dataset but goes one by one in the dataset and chooses how to fix the parameter **Θ** so that this data fits better in the algorithm.