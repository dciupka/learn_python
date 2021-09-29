# How zip works?
a = [1, 2, 3]
b = [4, 5, 6]

c = (list(zip(a,b)))

list_1 = [1,2,3]
list_2 = [3,4,5]

ziped = list(zip(list_1,list_2))


list_1, list_2 = zip(*ziped)

print(list(list_1))
print(list_2)

print(10 * "****")


names = ['dawid', 'mariola', 'mirek', 'marek', 'andrzej',]
surnames = ['ciupka', 'klimiuk', 'sowa', 'kryspinski', 'zigfido',]


name_surname = list(zip(names,surnames))


# Wynik
print(name_surname)


names_1, surnames_1 = zip(*name_surname)

print(names_1)
print(surnames_1)

