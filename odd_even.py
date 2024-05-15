# Author: Aayush Sharma
# Just for practice. Feel free to modify :)
# Code is explained in the comments ;]
import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid function (for backpropagation)
def sigmoid_derivative(x):
    return x * (1 - x)

# Input data (number represented as a binary vector)
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# Expected output (1 for odd, 0 for even)
y = np.array([[0], [1], [1], [0]])

# Initialize weights randomly with mean 0
np.random.seed(1)
weights_0 = 2 * np.random.random((3, 4)) - 1
weights_1 = 2 * np.random.random((4, 1)) - 1

# Training loop
for epoch in range(10000):
    # Forward propagation
    layer_0 = X
    layer_1 = sigmoid(np.dot(layer_0, weights_0))
    layer_2 = sigmoid(np.dot(layer_1, weights_1))

    # Backpropagation
    layer_2_delta = (layer_2 - y) * sigmoid_derivative(layer_2)
    layer_1_delta = layer_2_delta.dot(weights_1.T) * sigmoid_derivative(layer_1)

    # Update weights
    weights_1 -= layer_1.T.dot(layer_2_delta)
    weights_0 -= layer_0.T.dot(layer_1_delta)

# Test the trained network
print("Output:")
print(layer_2)