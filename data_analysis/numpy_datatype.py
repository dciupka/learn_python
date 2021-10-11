import numpy as np

print("jelzeli nie podam to int64")
a = np.array([1, 2, 3, 4])
print(a)
print(a.dtype)

print('zdefiniowany dtype=np.int16')
b=np.array([1, 2, 3, 4], dtype=np.int16)
print(b)
print(b.dtype)

print('float typ dtype = np.float64')

c = np.array([1, 2, 3, 4], dtype=np.float64)
print(c)
print(c.dtype)
