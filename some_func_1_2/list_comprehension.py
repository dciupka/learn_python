""" List comprehension is the most popular in Python functionality """
#----------------------------------------------------------------------------

customers = [("Dawid", 3000000),
	   ("Andrzej", 2000000),
           ("Maraian", 100000),
 	     ("Jerzy", 200000),
	    ("Stefan", 300000)]


big_whales  = [ f'{x} {y}' for x ,y in customers if y>1000000]

print('ALL', customers)
print('Duze ryby',big_whales)
print(100*'*')

#----------------------------------------------------------------------------

super_heros = [('Superman',20), ('Batman',30), ('Spiderman',50), ('Catgirl',25)]

sh  = [name for name, age  in super_heros if age<30 ]
print(sh) 
print(100*'*')
#----------------------------------------------------------------------------

salarys = {'Marian':10, 'Andrzej':20, 'Jozek':15}

ls_salary = [ name for name, sal in salarys.items() if sal <15]
print(ls_salary)


