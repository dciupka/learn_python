file_name = "open_file.py"

with open(file_name) as f:
	lines = []
	for l in f:
		lines.append(l.strip())
	print(lines)

