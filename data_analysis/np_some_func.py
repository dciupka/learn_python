import numpy as np
from random import randint
array_of_numbers = np.array([x for x in range(1,50)])

print(array_of_numbers)

index = randint(0,49)

for x in array_of_numbers:
	print(x)

