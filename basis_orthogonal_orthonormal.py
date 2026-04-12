import numpy as np

print("=== Basis, Orthogonal, and Orthonormal ===")

# 1) vectors i and j
i = np.array([1, 0])
j = np.array([0, 1])

print("i =", i)
print("j =", j)

# prove they are orthogonal
dot_ij = np.dot(i, j)
print("dot(i, j) =", dot_ij)

if dot_ij == 0:
    print("i and j are orthogonal")
else:
    print("i and j are NOT orthogonal")

# 2) vectors v and w
v = np.array([1, 2])
w = np.array([-2, 1])

print("v =", v)
print("w =", w)

# check if orthogonal
dot_vw = np.dot(v, w)
print("dot(v, w) =", dot_vw)

if dot_vw == 0:
    print("v and w are orthogonal")
else:
    print("v and w are NOT orthogonal")
