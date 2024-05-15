# Odd-Even Number Classifier using NumPy Neural Network

This Python code implements a simple neural network built from scratch using the NumPy library to classify whether a given number is odd or even.

## Description

The code defines a feedforward neural network with one input layer, one hidden layer, and one output layer. The input layer takes a binary representation of a number, and the output layer produces a value between 0 and 1, indicating whether the number is even (close to 0) or odd (close to 1).

The neural network is trained on a dataset of binary representations of numbers from 0 to 15, along with their corresponding labels (0 for even, 1 for odd). After training, the network can classify new numbers as odd or even by feeding their binary representation into the network and interpreting the output.

## Requirements

To run this code, you need to have Python 3 and NumPy installed on your system.

### Installing NumPy

If you don't have NumPy installed, you can install it using pip:

pip install numpy

## Usage

1. Clone or download the repository containing the code files.
2. Open a terminal or command prompt and navigate to the directory containing the code files.
3. Run the following command: On Windows and Mac ( python odd_even_v2.py ) or  for v1 ( python odd_even.py )
In linux python3 odd_even_v2.py or for v1 ( python3 odd_even.py )

4. The program will prompt you to enter a number or 'q' to quit.
5. After entering a number, the program will output whether the number is odd or even.

Here's an example run:

[output odd_even.py]:

Enter a number (or 'q' to quit): 7
Is 7 odd? yes
Enter a number (or 'q' to quit): 12
Is 12 odd? no
Enter a number (or 'q' to quit): q

## Code Explanation

1. The code starts by defining the sigmoid activation function and its derivative, which will be used in the forward and backward propagation steps.
2. The input data (`X`) and expected output (`y`) are defined as NumPy arrays.
3. The weights (`weights_0` and `weights_1`) for the neural network are initialized randomly with values between -1 and 1.
4. The training loop iterates for a fixed number of epochs (10,000 in this example).
5. In each epoch, the forward propagation step computes the output of the neural network given the input data and current weights.
6. The backpropagation step computes the gradients of the loss function with respect to the weights.
7. The weights are updated based on the computed gradients using the gradient descent algorithm.
8. After training, the `predict` function is used to classify new numbers as odd or even by feeding their binary representation into the trained neural network.
9. The user input loop prompts the user to enter a number, converts it to a binary vector, passes it through the neural network, and prints the classification result.

## Limitations

- This implementation is limited to classifying numbers between 0 and 15 due to the 4-bit binary representation used for the input.
- The neural network architecture is very simple, with only one hidden layer, which may not be sufficient for more complex tasks.
- The training time (10,000 epochs) may be insufficient for achieving optimal performance on larger input ranges or more complex tasks.

## Authors

- Aayush Sharma

## Note: 
None of the content is generated through AI.
