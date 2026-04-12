import numpy as np

print("=== Matrix Tensors ===")

# create matrix X with size 2x3
X = np.array([[1, 2, 3],
              [4, 5, 6]])

print("X =")
print(X)

# shape of X
print("shape of X =", X.shape)

# first column of X
print("first column of X =")
print(X[:, 0])

# second row of X
print("second row of X =")
print(X[1, :])
