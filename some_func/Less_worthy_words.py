
text = ("Johnny English (taglined in some countries as 'Little Brother of James Bond') is a 2003 spy comedy film directed by Peter Howitt and written by Neal Purvis, Robert Wade and William Davies. It is a British-French venture produced by StudioCanal and Working Title Films, and distributed by Universal Pictures." ) 

new_list = [[ x  for x in text.split() if len(x) > 3] for line in text.split('\n')]
print(new_list)




some_text = ("Mam na imie Dawid,\n i to tyel")
print(some_text)

n = [[ t for t in some_text.split()] for linie in some_text.split('\n')]
print(n)
