
Parametric Learning Algorithm is an algorithm that has a fixed set of parameters.

**Locally Weighted Regression** (LWR) is used when we want to have a curve as a result line instead of the linear line that we get from linear regression. This is used for data that is more define and and easily recognized as a curve line. LWR is a non-parametric learning algorithm which means that it doesn't have a fixed size of parameters (the number of parameters grows, with the size of data). 
It gets it name from using the local weights of the given data parameters. For example: 
If we have our data represented by x1,x2...xn then if we want to find value of y for our new value x we don't find the y value of the regression and then get the answer from there. We put more importance on the local xs. If for example our x is near x3,x4 then more importance is put on these parameters then on x10 or x1. This can be done by using the formula w(i) = exp(-(xi - x)^2 / 2)


Linear Regression is not a good algorithm for classification problems. 

Logistic Regression is the alternative for classification problems. 

**"Sigmoid" or "Logistic"** **function** is defined as **g(z) = 1/ (1 + e^(-z))**

In [numerical analysis](https://en.wikipedia.org/wiki/Numerical_analysis "Numerical analysis"), **Newton's method**, also known as the **Newton–Raphson method**, named after [Isaac Newton](https://en.wikipedia.org/wiki/Isaac_Newton "Isaac Newton") and [Joseph Raphson](https://en.wikipedia.org/wiki/Joseph_Raphson "Joseph Raphson"), is a root-finding algorithm which produces successively better approximations to the roots (or zeroes) of a real function ("Function (mathematics)"). The most basic version starts with a single-variable function _f_ defined for a real variable _x_, the function's derivative _f′_, and an initial guess x_0 for a root of _f_. If the function satisfies sufficient assumptions and the initial guess is close.


![[NewtonIteration_Ani.gif]]