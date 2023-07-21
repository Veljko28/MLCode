

## Chain Rule in Backprop

The chain rule is a fundamental concept used in backpropagation, which is the algorithm for training neural networks. It allows for the calculation of gradients or derivatives with respect to the weights and biases of each neuron in a neural network.

In backpropagation, the chain rule is applied to calculate the gradients of the loss function with respect to the parameters (weights and biases) of the network. These gradients are then used to update the parameters in the direction that minimizes the loss and improves the network's performance.

The chain rule states that if we have a function composed of multiple nested functions, the derivative of the composite function with respect to a parameter can be calculated by multiplying the derivatives of the inner functions with respect to that parameter.

## Activation Functions

- Sigmoid function
 Normalization of W: **w\[L] = np.random.randn(shape) \*  np.sqrt(1 /  n\[p-1])**

**- ReLU function**

Normalization of W:  **w\[L] = np.random.randn(shape) \*  np.sqrt(2 /  n\[p-1])**
 
The Rectified Linear Unit (ReLU) function is a popular activation function used in neural networks. It introduces non-linearity into the network, allowing it to learn complex patterns and make non-linear predictions.

The ReLU function is defined as follows:

f(x) = max(0, x)

In other words, the output of the ReLU function is zero for any negative input, and for positive inputs, it is equal to the input value itself. Mathematically, it can be represented as:

f(x) = { x, if x > 0; 0, otherwise }

The main advantage of the ReLU function is its simplicity and efficiency. The function is computationally inexpensive to evaluate and has a derivative that is either 0 or 1, making the gradient calculation straightforward during backpropagation.

ReLU activations help in mitigating the vanishing gradient problem, which can occur in deep neural networks when gradients become extremely small as they propagate backward through many layers. By preserving positive values, ReLU allows the gradients to flow more easily, promoting better learning in deep networks.

One limitation of ReLU is that it can cause "dead" neurons. If the input to a ReLU neuron is negative, the neuron remains inactive (outputting zero) and does not contribute to the learning process.
 
- Tanh function

The hyperbolic tangent function, commonly known as tanh, is an activation function used in neural networks. It is similar to the sigmoid function but scaled to have output values between -1 and 1.

The tanh function is defined as follows:

f(x) = (e^x - e^-x) / (e^x + e^-x)

In mathematical terms, the tanh function takes an input value x and maps it to an output value between -1 and 1. The function is symmetric around the origin, with a smooth S-shaped curve.

The tanh function has several properties that make it useful as an activation function in neural networks:

1. Non-linearity: Like other activation functions, tanh introduces non-linearity into the network, allowing it to learn complex relationships and make non-linear predictions.

2. Centered at zero: The tanh function has its mean centered at zero, meaning that its output is approximately zero when the input is close to zero. This can help in the convergence of the neural network during training.

3. Stronger gradients than sigmoid: Compared to the sigmoid function, the tanh function has steeper gradients, particularly for inputs further away from zero. This can accelerate learning in certain cases.


## Input Normalization

Input normalization, in simple terms, refers to the process of scaling and transforming the input data to have a consistent and standardized range. It aims to ensure that the features or variables used in a machine learning model are on a similar scale, which can lead to better model performance and stability.

Normalization is typically done by subtracting the mean of the data and dividing by the standard deviation. This process is known as standardization or z-score normalization. It transforms the data to have a mean of 0 and a standard deviation of 1.

## Vanishing & Exploding Gradients 

Vanishing and exploding gradients are common issues that can occur during the training of deep neural networks, especially those with many layers. These problems arise from the way gradients are propagated backward through the network during the backpropagation algorithm.

1. Vanishing gradients: In deep neural networks, gradients are backpropagated from the output layer to the input layer to update the weights. However, in networks with many layers, the gradients can become extremely small as they are multiplied by the weight matrices during backpropagation. Consequently, the gradients may approach zero, causing the network to learn very slowly or not at all. This is known as the vanishing gradient problem.

2. Exploding gradients: Conversely, exploding gradients occur when the gradients become extremely large during backpropagation. This can happen when the weight matrices have large values or when the network architecture has a high degree of connectivity. Large gradients can cause weight updates that are too drastic, leading to unstable training and difficulties in finding an optimal solution.


## Mini Batch Gradient Decent 

Mini-batch gradient descent is a variation of the gradient descent optimization algorithm used in machine learning for training neural networks and other models. It involves dividing the training data into smaller subsets called mini-batches and updating the model's parameters based on the average gradient computed from each mini-batch.

- Efficiency: It utilizes vectorized operations and parallel processing to perform computations on mini-batches efficiently, taking advantage of hardware acceleration.

- Noise reduction: Mini-batches provide a smoother estimation of the true gradient compared to using a single data point (stochastic gradient descent). This can lead to more stable and consistent updates.

- Generalization: Mini-batches provide a balance between the noisy updates of stochastic gradient descent and the slower but more accurate updates of batch gradient descent. This can help the model generalize well to unseen data.

## Momentum Algorithm

The momentum algorithm is an extension of the standard gradient descent optimization algorithm used to train machine learning models, including neural networks. It enhances the basic gradient descent by incorporating the concept of momentum to accelerate convergence and improve optimization performance.

In traditional gradient descent, the model parameters are updated based on the negative gradient of the loss function with respect to the parameters. The momentum algorithm introduces an additional term that accumulates the historical gradients to influence the direction and magnitude of the parameter updates. It makes predictions based on the previous predictions it made making less noise moving to the ideal parameter size.


The momentum algorithm helps accelerate the convergence of the optimization process in several ways:

- Smoothing updates: The momentum term smooths out the update process by averaging the gradients over time. It reduces the impact of noisy or erratic gradients, allowing for more stable and consistent updates.

- Accelerated updates: The momentum term accumulates gradients across iterations and amplifies the updates in the direction of consistent gradients. This can help the algorithm escape shallow local minima and traverse flat regions more quickly.
   
- Enhanced learning in plateaus: In flat regions or plateaus of the loss landscape, where the gradients become small, the momentum term can push the optimization process forward by preserving and accumulating previous gradients.