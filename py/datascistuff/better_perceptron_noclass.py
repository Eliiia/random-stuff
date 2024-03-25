import numpy as np
import matplotlib.pyplot as plt
import random
import math

# following tutorial 
# https://python.plainenglish.io/building-a-perceptron-from-scratch-a-step-by-step-guide-with-python-6b8722807b2e
# !!!
# see better_perceptron_class.py

# define inputs
x = [1,0]

# generate initial weights
w = []
nInputs = len(x) 
for i in range(nInputs): # for each input
    w.append(random.uniform(-1, 1)) # ...generate random weights between -1 and 1

# and bias!
b = random.uniform(-1, 0)

# used to determine whether output should be 1 or 0 with uncertainty in the middle
def sigmoid(x):
    return 1/(1+math.exp(-x))

# activation function
# defines whether output is 0 or not based on confidence from sigmoid function
# z is a number from sigmoid function
def activation(z):
    return 1 if z >0.5 else 0

# define output
y = 1

# training
for i in range(0,10):
    # feed forward; pass input data through perceptron 
    # calculate weighted sum of inputs, pass result through sigmoid function
    z = sigmoid(np.dot(x, w) + b) # weighted sum = w1*x1 + w2*x2 ... + b (dot product)

    # predict
    y_pred = activation(z)
    error = y - y_pred

    print(f"Correct: {y == y_pred}, y={y}, y_pred={y_pred}")
    print(f"old w: {w}, old b: {b}")

    lr = 0.1 # learning rate, can change based on problem
    # calculate new values
    new_w = []
    for wi, xi in zip(w, x):
        new_w.append(wi + lr * error * xi)
    new_b = b + lr * error

    w = new_w
    b = new_b

    print(f"new w: {w}, new b: {b}")


