""" List comprehension is the most popular in Python functionality """

customers = [("Dawid", 3000000),
	   ("Andrzej", 2000000),
           ("Maraian", 100000),
 	     ("Jerzy", 200000),
	    ("Stefan", 300000)]


big_whales  = [ f'{x} {y}' for x ,y in customers if y>1000000]

print('all', customers)
print('Duze ryby',big_whales)
