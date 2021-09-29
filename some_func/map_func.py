print(100*'--')
print([line.strip() for line in open('map_func.py')]) #wczytanie tego pliku

txt = ['Funkcja lambda to funkcje anonimowe',
	'Funkcje anonimowe nie maja nazwy',
	'Funkcje w Pythonie sa obiektami.']

mark = map(lambda s : (True,s) if 'anonimowe' in s else (False, s), txt)
print(list(mark))
print(10*'---')

Nie = 'nie'
Tak = 'tak'
nie = map(lambda word : (Nie, word) if 'nie' in  word else (Tak, word), txt)
print(list(nie))

