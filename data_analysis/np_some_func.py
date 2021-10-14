import numpy as np
from random import randint, choice
liczby_do_wylosowania = [x for x in range(1,50)]
zakres = 49
# lotto funkcja z np
pusta_lista =[]
for losowanie in range(1,7):
	index=randint(1,zakres)
	zakres-=1
	liczba=liczby_do_wylosowania.pop(index)
	pusta_lista.append(liczba)
if len(set(pusta_lista))>=6:
	a = np.array([pusta_lista])

print(a)
