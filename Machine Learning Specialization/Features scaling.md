# Features scaling

We can normalize in two ways:
1. By dividing the numbers by the maximum value that way we get all the numbers between 0 and 1
2. By using mean normalization, we do this by calculating the mean (average) μ of all the values and the calculating with the next formula x1 = x1 - μ1 / max - min, where max is the maximum value of the array and min is the minimum. This way all the values fall between -1 and 1 on both the x and y axis.
3. Z-score - by dividing the difference between the value and the mean of the array by the standard deviation of the current value. x1 = x1 - μ1  / σ1.

## How to check if gradient descent is converging?

Draw a learning curve in order to check when you can stop doing gradient descent. When the line gets flat or close to flat is when you should consider stopping.

Automatic convergence test: let ε be 10^(-3).

If J(w, b) decreases by <= ε in one iteration, declare convergence. 

## How to choose a good learning rate?

If the learning rate is too large you will see that the cost function will have bums, where it goes up and then down, or it'll just be increasing in which case you can be certain that the learning rate is really bad. To fix this we choose the learning rate to be a really small number, something lower than 1 usually around 0.01 or 0.001.
