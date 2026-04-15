import numpy as np

print("=== Basis, Orthogonal, and Orthonormal ===")

# Question 1: Create vectors i and j
i = np.array([1, 0])
j = np.array([0, 1])

print("i =", i)
print("j =", j)

# Check orthogonality using dot product
dot_ij = np.dot(i, j)
print("dot(i, j) =", dot_ij)

# If dot product = 0 → orthogonal
if dot_ij == 0:
    print("i and j are orthogonal")
else:
    print("i and j are NOT orthogonal")

print("----------------------------------")

# Question 2: Check vectors v and w
v = np.array([1, 2])
w = np.array([-2, 1])

print("v =", v)
print("w =", w)

# Compute dot product
dot_vw = np.dot(v, w)
print("dot(v, w) =", dot_vw)

if dot_vw == 0:
    print("v and w are orthogonal")
else:
    print("v and w are NOT orthogonal")
