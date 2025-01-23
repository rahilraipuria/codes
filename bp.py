import numpy as np

sigmoid = lambda x: 1 / (1 + np.exp(-x))
sigmoid_derivative = lambda x: x * (1 - x)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

w1, w2 = np.random.rand(2, 2), np.random.rand(2, 1)
b1, b2 = np.random.rand(1, 2), np.random.rand(1, 1)
lr, iter = 0.1, 10000

for _ in range(iter):
    h = sigmoid(X.dot(w1) + b1)
    o = sigmoid(h.dot(w2) + b2)
    e = y - o
    o_delta = e * sigmoid_derivative(o)
    h_delta = o_delta.dot(w2.T) * sigmoid_derivative(h)
    w1 += X.T.dot(h_delta) * lr
    w2 += h.T.dot(o_delta) * lr
    b1 += h_delta.sum(axis=0, keepdims=True) * lr
    b2 += o_delta.sum(axis=0, keepdims=True) * lr

print(o)