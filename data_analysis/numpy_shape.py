import numpy as np

a = np.array([1,2,3,4])

print(a)
print('cztery itemy, w jednym wierszu')
print(a.shape)
print("******************************")


b = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(b)
print(b.shape)

print("******************************")

c = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print(c)

print('shape ',c.shape)
print('dim ',c.ndim)
