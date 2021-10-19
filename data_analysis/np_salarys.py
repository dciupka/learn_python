import numpy as np

# Data
alicja = [99, 101, 103]
robert = [110, 108, 105]
tomasz = [90, 88, 85]


names = np.array(['alicja', 'robert', 'tomasz'])
salaries = np.array([alicja, robert, tomasz])
taxation = np.array([[0.2, 0.25, 0.22],
			[0.4, 0.5, 0.5],
			[0.1, 0.2, 0.1]])

taxed = np.array(salaries - salaries * taxation)
## One line coode
max_income = np.max(salaries - salaries * taxation)

big_whale =set(names[np.nonzero(taxed == max_income)[0]])
## Wynik
print(max_income)
print(taxed)
print(big_whale)


listaX = np.array([2,3,4,5])
print(names[np.nonzero(taxation>0.3)[0]])
