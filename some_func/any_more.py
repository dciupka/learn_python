
test_list = [4, 5, 0, 9,20,30]

print('The original list ' + str(test_list))

# any (warunek dla np listy)
res = any( 34< element for element in test_list)
print(res)

names = ['daiwd', 'mariola','bonie']

print('Names in the list' + str(names))

check = any( 'bonie'== element for element in names)

print(check)

print(10*'---')

def any(lista):
	for item in lista:
		if item:
			return True
	return False

empty  = []

print(any(names))
print(any(empty))
