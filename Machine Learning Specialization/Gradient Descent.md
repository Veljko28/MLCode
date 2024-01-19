# Gradient Descent

Gradient descent is an algorithm that reduces the value of any given function. It tweaks the parameters w and b to find the smallest value of the function. 

w = w-α d/dw J(w, b) - where α is the learning rate
b = b-α d/db J(w, b)

Repeat until convergence. Convergence meaning the parameters w and b not longer change for the given formulas.
The values will need to be updated at the same time, not one by one.

By calculating the derivative we get the slope of the current position. multiplying it with the learning rate we adjust the new value of the parameter that is closer to the minimum. 
If the minimum of the function requires a larger parameter than the current one the derivative will be negative and we would just add to the parameter to get the better value (the one closer to the minimum).

As we approach the local   minimum the update value gets smaller and smaller, because the derivative value gets smaller (closer to zero), The gradient descent algorithm stops when the derivative gets to 0, because it sets w = w -  α\*0 


Batch gradient descent refers to the gradient descent algorithm that uses all the training examples.
