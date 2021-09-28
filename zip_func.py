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
