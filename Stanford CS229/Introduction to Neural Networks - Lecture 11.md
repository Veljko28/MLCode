
## Logistic Regression Networks

In an LRN, the logistic regression model is integrated into the neural network framework by using logistic activation functions at the output layer. This allows the network to output probabilities or class probabilities for each class, similar to logistic regression. The input features are fed through multiple hidden layers, enabling the network to learn hierarchical representations and capture nonlinear relationships in the data.

## Cross-entropy loss function (softmax)

The cross-entropy loss function is a commonly used objective or loss function in machine learning, particularly for classification tasks. It measures the dissimilarity between predicted probabilities and the true labels of the data.

In binary classification, the cross-entropy loss is calculated as:

L = -\[y * log(p) + (1 - y) * log(1 - p)]

where:

- L is the loss,
- y is the true label (0 or 1),
- p is the predicted probability of the positive class.

In multi-class classification, the cross-entropy loss is a generalization of the binary case. It sums the individual cross-entropy losses for each class label. It can be formulated as:

L = -∑\[y * log(p)]

where the summation is performed over all classes.

The cross-entropy loss penalizes large differences between predicted and true probabilities. It encourages the model to assign higher probabilities to the correct class and lower probabilities to incorrect classes. By minimizing the cross-entropy loss during training, the model learns to make more accurate predictions and improves its ability to discriminate between different classes.

## Neural Networks

Neural networks, also known as artificial neural networks (ANNs), are a class of machine learning models inspired by the structure and function of biological brains. They are composed of interconnected artificial neurons (also called nodes or units) organized into layers.

Neural networks consist of an input layer, one or more hidden layers, and an output layer. Each neuron in a layer receives inputs, performs a weighted sum of those inputs, applies an activation function to produce an output, and passes it to the neurons in the next layer. The weights associated with the connections between neurons are learned during the training process.

The activation function introduces non-linearity into the network, allowing it to learn complex relationships and make non-linear predictions. Common activation functions include sigmoid, tanh, and rectified linear unit (ReLU).

Neural networks are highly flexible and can be used for various machine learning tasks, including classification, regression, and even tasks like image and speech recognition. Deep neural networks, which have multiple hidden layers, have gained significant attention and have achieved state-of-the-art performance in many domains, often referred to as deep learning.

## Backward propagation 

Neural networks learn by adjusting the weights through a process called backpropagation. In training, the network compares its predicted outputs with the true labels of the training data and calculates a loss or error. This error is then propagated backward through the network, updating the weights using optimization algorithms such as stochastic gradient descent (SGD) to minimize the error.
