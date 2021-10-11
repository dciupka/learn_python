'''Dependencies'''
import numpy as np

# data salary in [2025, 2026, 2027]

dataScientist =  [130, 132, 137]
productManager = [127, 140, 145]
designer =       [118, 118, 127]
softwareEngineer=[129, 131, 137]

employees = np.array([dataScientist, productManager, designer,softwareEngineer])

print(employees)

employees[0,::2] = employees[0,::2] *1.1

print(employees)

