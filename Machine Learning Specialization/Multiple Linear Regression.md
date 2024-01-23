# Multiple Linear Regression

Multiple linear regression is the same model as linear regression but it has more than one input feature.

It's formula is: f(x) = w1x1 + w2x2 + ... wnxn + b
where: w1x1 + w2x2 ... is the dot product of vectors w and x.

## Vectorization 

To use vectors for the dot product we can use the numpy library and its np.dot(w, x) function for faster computation.
f(x) = w • x + b;

## Gradient descent with MLR

When different features have different ranges of values it can cause gradient descent to bounce around and have a hard time getting to the local minimum.
In order to prevent this we want to rescale the features so that they fit the same range and that way we get better predictions and faster gradient descent. 
