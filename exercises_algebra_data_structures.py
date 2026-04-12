import numpy as np

print("=== Exercises on Algebra Data Structures ===")

# Question 1: Transpose of vector
v = np.array([[25],
              [2],
              [-3],
              [-23]])

print("Original vector =")
print(v)

print("Transpose =")
print(v.T)


# Question 2: Dimensions of matrix Y
Y = np.array([[42, 4, 7, 99],
              [-99, -3, 17, 22]])

print("\nMatrix Y =")
print(Y)

print("Dimensions of Y =", Y.shape)


# Question 3: Position of 17
print("\nPosition of 17 in Y is Y[2,3] (row 2, column 3)")
