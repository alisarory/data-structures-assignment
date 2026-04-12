import numpy as np

print("=== Norms and Unit Vectors ===")

# 1) create vector x with size 3x1
x = np.array([[1],
              [2],
              [3]])

print("vector x =")
print(x)

# L2 norm of vector x
norm_x = np.linalg.norm(x)
print("L2 norm of x =", norm_x)

# 2) create vector v with elements (3,4)
v = np.array([3, 4])
print("vector v =", v)

# L2 norm of vector v
norm_v = np.linalg.norm(v)
print("L2 norm of v =", norm_v)

# unit vector of v
unit_v = v / norm_v
print("unit vector of v =", unit_v)

# length of unit vector
print("length of unit vector =", np.linalg.norm(unit_v))
