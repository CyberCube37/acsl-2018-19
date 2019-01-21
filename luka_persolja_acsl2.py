# Luka Peršolja
# Gimnazija Vič, 2.b (grade 10)
# Intermediate 3
# Language: Python 3.7

import fileinput

def difference(a, b):
	comm = ""
	for i in a:
		for n, j in enumerate(b):
			if i == j:
				b = b[n+1:]
				comm += j
				break
	return comm


for line in fileinput.input():
	a, b = str(line).split()
	c, d = a[::-1], b[::-1]
	chrs = list(set(difference(d, c)) & set(difference(c, d)) & set(difference(b, a)) & set(difference(a, b)))
	chrs.sort()
	if chrs:
		print("".join(chrs))
	else:
		print("NONE")