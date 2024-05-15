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
X = np.array([[0, 0, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 1, 0],
              [0, 0, 1, 1],
              [0, 1, 0, 0],
              [0, 1, 0, 1],
              [0, 1, 1, 0],
              [0, 1, 1, 1],
              [1, 0, 0, 0],
              [1, 0, 0, 1],
              [1, 0, 1, 0],
              [1, 0, 1, 1],
              [1, 1, 0, 0],
              [1, 1, 0, 1],
              [1, 1, 1, 0],
              [1, 1, 1, 1]])

# Expected output (1 for odd, 0 for even)
y = np.array([[0], [1], [1], [0], [1], [0], [0], [1], [1], [0], [0], [1], [0], [1], [1], [0]])

# Initialize weights randomly with mean 0
np.random.seed(1)
weights_0 = 2 * np.random.random((4, 4)) - 1
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

# Function to convert a number to a 4-bit binary vector
def number_to_vector(num):
    vector = [int(bit) for bit in f"{num:04b}"]
    return np.array(vector)

# Function to predict if a number is odd or even
def predict(num):
    input_vector = number_to_vector(num)
    layer_0 = input_vector
    layer_1 = sigmoid(np.dot(layer_0, weights_0))
    layer_2 = sigmoid(np.dot(layer_1, weights_1))
    if layer_2 >= 0.5:
        return "yes"
    else:
        return "no"

# Get user input and make a prediction
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    if not user_input:
        print("Invalid input. Please enter a number or 'q' to quit.")
        continue
    try:
        num = int(user_input)
        result = predict(num)
        print(f"Is {num} odd? {result}")
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")