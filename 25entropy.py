# 25entropy.py by Khalid Saif Co-authored with Ethan Djou

import math

def shannon(a, c, g, t):
	total = a + c + g + t
	pa = a / total
	pc = c / total
	pg = g / total
	pt = t / total
	
	entropy = 0
	if a != 0: entropy = entropy + a * math.log2(pa)
	if c != 0: entropy = entropy + c * math.log2(pc)
	if g != 0: entropy = entropy + g * math.log2(pg)
	if t != 0: entropy = entropy + t * math.log2(pt)
	return -entropy
	
	
# Testing the formula
print(shannon(13, 14, 15, 16))
print(shannon(25, 80, 55, 100))
print(shannon(6, 143, 157, 0))
print(shannon(6785, 7, 0, 879))
print(shannon(968, 0, 365, 9))
print(shannon(0, 7, 5, 4))


