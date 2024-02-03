#scoringmatrix by Khalid Saif

nts = 'ACGT'										#Horizontal header
print('   ', end='')
for i in nts:
	print(i, end='  ')
print()

for nt1 in nts:
	print(nt1, end=' ')
	for nt2 in nts:
		if nt1 == nt2: print('+1', end=' ')
		else 		 : print('-1', end=' ')
	print()

"""
	A  C  G  T										#indented instead of 4 spaces
A +1 -1 -1 -1
C -1 +1 -1 -1
G -1 -1 +1 -1
T -1 -1 -1 +1
"""