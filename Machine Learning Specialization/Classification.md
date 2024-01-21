# Classification

Binary classification is when we have only 2 classes (usually something like yes/no, true/false).

### Why not linear regression?

Fitting a line through this type of data will cause bad results, basically we want to group the classes and not draw a line trough all of them, that would just be a bad idea.

if f(x) < 0.5 -> y_hat = 0
if f(x) >= 0.5 -> y_hat = 1
This is using something called a threshold value, which is a value we set in order to divide the classes. For example if you want to get on a ride in Disneyland you have to be taller than 150cm to get on, 150cm in this case would be the threshold value.

## Logistic Regression

To use logistic regression we will use something called a **sigmoid function**. The formula for a sigmoid function is 1/1+e^(-z), where z in this case would be a line that we previous saw, something like z = w • x + b. The sigmoid function is also called the logistic function. 
