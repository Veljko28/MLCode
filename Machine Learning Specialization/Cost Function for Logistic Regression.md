# Cost Function for Logistic Regression

The squared error cost function is not an ideal function for logistic regression. The reason why is that the sigmoid function is not convex, so there are a lot of local minimums that you can get stuck in.

In this case we use a different loss function. if y^i = 1 the loss is equal to -log(f(x)).
All output y values are between 0 and 1 so we should only look at -log() between 0 and 1. For these values -log is positive and decreases to zero when approaching 1 so the close the predicted value is to 1 the smaller the cost. 
If y^i = 0 then we use the formula -log(1-f(x)). This is the same thing but flipped so that the loss is equal to 0 when the predicted loss is 0 and the further away the greater the loss.

The formula for logistic loss can be written this way:
L(f(x^i), y^i) = -(y^i)log(f(x^i)) - (1-y^i)log(1 - f(x^i)).

Basically an activation function so if y = 1 the first part activates and the other goes to 0 and if y = 0 the first part is 0 and the second part activates (gets multiplied by 1).
