# Cost Function

How do we find w and b so that y-hat is close to y^i for all (x^i, y^i) ?

The cost function takes y-hat and compares it to the target y.
(y-hat - y) is the error

We can also compute the squared error:
J(w,b) = 1/m * Sum (y-hat^i- y^i)^2
m - number of training examples

J(w,b) is the squared error cost function

We want to minimize the function J, by tweaking the parameters w and b. We can do this by visualizing the sets of values in a 3D plane and getting the minimum. Sometimes this isn't possible to visualize but we can get the local minimum programmatically. 
