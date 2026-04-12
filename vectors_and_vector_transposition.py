import numpy as np

print("=== Vectors and Vector Transposition ===")

# 1) create vector x with size 3x1
x = np.array([[1],
              [2],
              [3]])

print("vector x =")
print(x)

# length of vector x
print("length of x =", len(x))

# shape of vector x
print("shape of x =", x.shape)

# type of vector x
print("type of x =", type(x))

# first element of vector x
print("first element of x =", x[0, 0])

# type of first element
print("type of first element =", type(x[0, 0]))

# 2) transpose x and save in x_t
x_t = x.T
print("transpose of x =")
print(x_t)

# shape of x_t
print("shape of x_t =", x_t.shape)

# create vector y and transpose it
y = np.array([[4],
              [5],
              [6]])

y_t = y.T
print("transpose of y =")
print(y_t)

# shape of y_t
print("shape of y_t =", y_t.shape)
