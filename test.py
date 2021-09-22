
text = ['Funkcje lambda to funkcje anonimowe', 'Funkcje anonimowe nie maja nazwy',
	'Funkcje w pythonie sa obiektami']

new = [ (True,item) if 'nie' in item  else (False, item) for item in text]

print(new)
