import numpy as np

a  = np.array([55, 56, 57, 58, 59, 60, 61])
print(a)
print(a[::2])
print(a[2:])
print(a[::-1])
print("--------")

b = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])

print(b)
print('***********')
print(b[1, :])
print('***********')
print(b[0,::-1])
print('***********')
print(b[::-1,::-1])
