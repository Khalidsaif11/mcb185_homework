# 30demo.py by Khalid Saif

#while loops

"""
while True:
	print('hello')								#Never ending loop(put"to inactivate))
"""

i = 0
while True:										#break the loop
	i = i + 1
	print('hey', i)
	if i == 3: break

i = 0
while i < 3:									#provide a condition as break
	print(i)
	i = i + 1
print('final value of i is', i)

i = 1
while i < 10:									#different start, limit, & increment
	print(i)
	i = i + 3
print('final value of i is', i)


#for i in range() loops

for i in range(1, 10, 3):
	print(i)

for i in range(5):								#normally increment 1 & start 0
	print(i)

"""
for i in range(5): print(i)						#same thing!
for i in range(0, 5): print(i)
for i in range(0, 5, 1): print(i)
"""


#for item in container							#how many characters

for char in 'hello':
	print(char)

seq = 'GAATTC'
for nt in seq:
	print(nt)
	

for nt1 in 'ACGT':								#nested loops!
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else		 : print(nt1, nt2, '-1')

"""												#assigning long characters to a variable
nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')
"""

limit = 4										#getting uniqe combinations only
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)

#Algorithms

def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total

print(gc_comp('ACAGCGAAT'))


#Practice Problems

def triangular(n):								#triangular function
	tri = 0
	for i in range(n + 1):
		tri = tri + i
	return tri
print(triangular(5))

def factorial(n):								#Factorial function
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
print(factorial(5))
print(factorial(0))


def euler(limit):								#Euler estimation function
	e = 0
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e
print(euler(5))
print(euler(2))


import math

def is_perfect_square(n):						#perfect square function
	root = math.sqrt(n)
	if math.isclose(root, root // 1): return True
	return False
print(is_perfect_square(4))
print(is_perfect_square(8))


def is_prime(n):								#prime function
	for den in range(2, n//2):
		if n % den == 0: return False
	return True
print(is_prime(2))
print(is_prime(25))