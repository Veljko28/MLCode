# Polynomial Regression
Using polynomial regression we can better fit the data by raising the input features to the power and getting a curved line.
This curved line in most cases fits the data better than just a straight line.

Example:
F(x) = w1x + w2x^2 + w3x^3 + b

Because we are using numbers to the power of something we will usually get really big numbers and the numbers
will have a large difference between one another. It is important to use feature scaling so that w3x^3 is as close to w1x as possible.
