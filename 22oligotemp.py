# 22oligotemp.py by Khalid Saif co-authored with Ethan Djou

def oligo(a, c, g, t):				#oligo melting temperature
	if A + T + G + C <= 13:
		return (A + T) * 2 + (G + C) * 4
	else: 
		return 64.9 + 41*(G + C - 16.4) / (A + T + G + C)
print(oligo(1, 2, 2, 2))
print(oligo(15, 100, 24, 62))
print(oligo(5, 6, 7, 8))