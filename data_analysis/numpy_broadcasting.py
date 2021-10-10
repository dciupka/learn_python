import numpy as np

# one dimension array 
a = np.array([1, 2, 3, 4])

print(a.ndim)

# two dimension array
b = np.array([[2, 1, 2], [3, 2, 3], [4, 3, 4]])

print(b.ndim)

# three dimension array
c =  np.array([[[2, 1, 2], [3, 2, 3], [4, 3, 4]],
[[2, 1, 2], [3, 2, 3], [4, 3, 4]]])

print(c.ndim)

