import numpy as np
import matplotlib.pyplot as plt
import random
import math

#from sklearn import datasets
#iris = datasets.load_iris()

# following tutorial 
# https://python.plainenglish.io/building-a-perceptron-from-scratch-a-step-by-step-guide-with-python-6b8722807b2e
# !!!
# see better_perceptron_noclass.py

# modified/expanded on

def sigmoid(x):
    return 1/(1+math.exp(-x))

class Perceptron():
    def __init__(self, input_size = 2, lr = 0.01, epochs = 20):
        self.lr = lr
        self.epochs = epochs
        self.input_size = input_size
        self.w = np.random.uniform(-1, 1, size=(input_size))
        self.bias = random.uniform(-1,0)
        self.misses = []

    def predict(self, x):

        w = self.w
        b = self.bias
        z = sigmoid(np.dot(x, self.w) + b)

        return 1 if z>0.5 else 0

    def fit(self, x, y):

        for epoch in range(self.epochs):
            miss = 0
            for yi, xi in zip(y, x):
                # predict
                y_pred = self.predict(xi)

                # update weights!
                error = yi - y_pred
                self.w += self.lr*error*xi
                self.bias += self.lr*error
                miss += int(error != 0.0)
            # for each epoch, get number of classifications
            self.misses.append(miss)

# ---

# import dataset
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target

# get only part of dataset
X = X[:100, [0,2]]
y = y[y<2]

# run perceptron based on data
p1 = Perceptron(2, 0.01, 20)

p1.fit(X, y)
print(p1.w, p1.bias)
#p.predict(X, y)

print(p1.misses)

# ---

# run perceptron based on own dataset
p2 = Perceptron(2, 0.1, 20)

X = np.array([[0,1], [0,0], [0,1], [1,1], [1,0], [0,0], [0,1], [1,1], [1,0]])
y = np.array([1,1,1,0,0,1,1,0,0]) # first number being 0 defines success

p2.fit(X, y)
print(p2.w, p2.bias)
#print(p.predict(np.array([1,0])))


# ---

# plot misses plots
print("dataset misses", p1.misses)
plt.subplot(1,2,1) # show on left side of screen
plt.title("dataset misses")
plt.plot(range(len(p1.misses)), p1.misses)
plt.ylabel("misses")
plt.xlabel("epoch")

print("custom data misses", p2.misses)
plt.subplot(1,2,2) # show on left side of screen
plt.title("custom data misses")
plt.plot(range(len(p2.misses)), p2.misses)
plt.ylabel("misses")
plt.xlabel("epoch")

plt.tight_layout() # show a bit nicer
plt.show()