import numpy as np
from random import randint
ars = np.array([x for x in range(1,50)])

index = randint(0,49)

#drawed_numbers= np.array([ars[index],ars[index]])

drawed_numbers= np.array([[ars[randint(0,49-x)] for x in range(1,7)] for los in range(0,1000000)])
print(drawed_numbers)
