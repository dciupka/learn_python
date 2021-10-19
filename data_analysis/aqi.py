import numpy as np

#x = np.array([[1, 0, 0], [0, 2, 2], [3, 0, 0]])
#print(x)
#print(10*'--')
#print(np.nonzero(x))
#print(10*'--')
#print(x==2)


X = np.array(
	[[42,40,41,43,44,43],
	 [30,31,29,29,29,30],
	 [8,13,31,11,11,9],
	 [11,11,12,13,11,12]])
print(X)
print('average:')
print(np.average(X))

cities = np.array(['honkong', 'nowy york', 'berlin', 'montreal'])
polluted = set(cities[np.nonzero(X> np.average(X))[0]])
print(polluted)



print(cities[np.nonzero(X>np.average(X))[0]])

print(10*'--')

print(np.nonzero(X>np.average(X)))

