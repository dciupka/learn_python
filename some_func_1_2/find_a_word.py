""" funkcja find wyszukuje slowo kluczoe plus 18 i minus 18 znakow """

 
text = ' Amazon od lat był obecny w Polsce – za sprawą swoich centrów logistycznych i rozwojowych.'

finde = lambda w, t: t[t.find(w)-18:t.find(w)+18] if w in t else -1

print(finde('kupa', text))




