


#Dane
firmy = {
	'Fajna_firma' : { 'alicja':30, 'bob':20, 'zenon':40 },
	'3M' : {'dawid': 2, 'tomek':20, 'janek':40},
	'Volvo' : {'jan':4, 'marian':10, 'zdzichu':22, 'ewa':22},
	}

##Jednowierszowiec

illegal =  [ firma for firma in firmy if any(zarobek<10 for zarobek in firmy[firma].values())]

sum_sallary = [ (firma, sum(sum_zar.values())) for firma,sum_zar in firmy.items()]

grube_ryby =  [ firma for firma in firmy if any(zarobek>31 for zarobek in firmy[firma].values())]
#Wynik
print(illegal)
print(sum_sallary)
print(grube_ryby)
#test any

#print(sum([x*x for x in range(20)])) # to jest lista skaladana
#print(sum(x*x for x in range(20))) #to jest generator


print(any(y>100 for y in range(20)))
print(any(y<100 for y in range(20)))

