# F = (Cx9/5) +32


# first proposition 
"""
def c2f(*args):
	lista = []
	for arg in args:
		new = arg*(9/5)+32	
		lista.append(new)
	return lista	
"""	




# second propositon with use map()
'''
def conv(x):
	return x*(9/5)+32

def c2f(*args):
	return list(map(conv,args))

'''




#test
f_lst = c2f(-272, 0 ,36 ,100)
print(f_lst) # expected output [-457.6, 32.0, 96.8, 212.0]



