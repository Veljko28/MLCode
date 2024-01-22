# Overfitting & Underfitting

Overfitting means that the predicted values of the algorithm fit the data extremely well, to the point that it doesn't generalize well, and it has high variance. Overfitting usually occurs because we use to many parameters that influence the result.
 
Underfitting means that the predicted values of the algorithm don't fit well the training set. It can also be called high bias. By underfitting we use too little parameters, even some might be left out, that is why we get high bias.


Some ways to deal with overfitting are:
- get more data
- see if you can use fewer features
- regularization 

## Regularization

 The idea of regularization is to reduce the values of the parameters w and b. It makes for a simpler model and is less likely to overfit the data.
λ - Regularization hyper-parameters. λ > 0

Regularization is added to the loss function as follows:

J(w,b) = 1/2m Sum(f(x)-y)^2 + λ/2m Sum(w^2).  
