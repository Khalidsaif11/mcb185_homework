#40demo.py by Khalid Saif

import random

for i in range(5):							#produce 5 different numbers within 0<x<1
	print(random.random())

for i in range(50):
	print(random.choice('ACGT'), end='')	#random 50 characters from a container
print()										


for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='')		#70% AT
	else:       print(random.choice('CG'), end='')
print()


for i in range(3):							#rolling a dice 3 times
	print(random.randint(1, 6))				#inclusive end points


for i in range(5):
	print(random.gauss(0.0, 1.0))			#mean & SD of normal distribution


print('this line\n has some\n line breaks')	#\n for line breaks or enter

print('a\tb\tcat\tdogma')					#tab key \t for spaces horizontally

print(10, 20, 30, 40, sep='\t')
print(100, 2000, 30000, 40000, sep='\t')	#sep='\t' for seperation by spaces


i = 1										#f string
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')

print(f'formatted string {i} {pi:.3f}')		#:.3f for rounding 3 decimal places

import sys									#keep the logging in terminal

print('logging', file=sys.stderr)

random.seed(1)								#if you want fixed set of numbers instead of random
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

