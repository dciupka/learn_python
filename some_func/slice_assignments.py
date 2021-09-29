visitors = ['Firefox', 'uszkodzone', 'Chrome', 'uszkodzone', 'Safari', 'uszkodzone', 'Mozzila', 'uszkodzone',]

visitors[1::2] = visitors[::2]
print(100*'*')
print(visitors)

print(100*'*')

lista = [1,2,3,4,5,6]

lista[1::1] = lista[::2]
print(lista)
