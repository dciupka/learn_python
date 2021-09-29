#Dane
firmy = {
        'Fajna_firma' : { 'alicja':30, 'bob':20, 'zenon':40 },
        '3M' : {'dawid': 2, 'tomek':20, 'janek':40},
        'Volvo' : {'jan':4, 'marian':10, 'zdzichu':22, 'ewa':22},
        }


lista = [firma for firma in firmy if any(price<10 for price in firmy[firma].values())]
print(lista)
