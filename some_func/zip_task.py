# Data
column_names = [ 'name',  'salary', 'job']
db_rows = [('Alicja', 180000, 'analityk danych'), ('Robert', 20000, 'python dev'),('Marian', 40000, 'wozny')]


dictionary = [dict(zip(column_names,dic)) for dic in db_rows]

print(dictionary)
