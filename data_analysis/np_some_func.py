import numpy as np
from random import randint, choice
ars = [x for x in range(1,50)]

index = randint(0,49)



#drawed_numbers= np.array([ars[index],ars[index]])

drawed_numbers= np.array([[ars.pop(randint(0,48-x)) for x in range(1,7)] for los in range(0,10000)])
for i in drawed_numbers:
	print(set(i))
