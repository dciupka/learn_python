
def square(x):
	return x*x

numbers = [1,2,3,4,5,6]

print(tuple(map(square,numbers)))
print(set(map(lambda x: x*x,numbers)))




