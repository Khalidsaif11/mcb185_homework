#33triples by Khalid Saif Co-authored with Natnael Tsegai

for a in range(1, 100):
	for b in range(a, 100):
		c = (a**2 + b**2)**0.5
		if c == c // 1 and a == a // 1 and b == b // 1: print("triples", a, b, c)