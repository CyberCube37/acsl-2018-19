# Luka Peršolja
# Gimnazija Vič, 2.b (grade 10)
# Intermediate 3
# Language: Python 3.7

import fileinput

for line in fileinput.input():
	st, n = str(line).split()
	n = int(n)
	vsota = 0

	while len(st) >= n:
		a = st[0:n]
		vsota += int(a)
		st = st[1:]

	print(vsota)
