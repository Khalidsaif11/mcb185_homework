#savingthrows.py by Khalid Saif co-authored with Ethan Djou & George Mo

import random

trials = 1000										#DC of 5, 10, & 15

print('DC\tadv')
for i in range(5, 16, 5):							#advantage take highest
	print(i, end='\t')
	success = 0
	for n in range(trials):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 > d2: 
			a = d1
		else: 
			a = d2
		if a >= i:
			success += 1
	print(success / trials)
print('\n')


print('DC\tdis')
for i in range(5, 16, 5):							#disadvantage take lowest
	print(i, end='\t')
	success = 0
	for n in range(trials):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 < d2:
			a = d1
		else:
			a = d2
		if a >= i:
			success += 1
	print(success / trials)
print('\n')


print('DC\tnorm')
for i in range(5, 16, 5):							#normal
	print(i, end='\t')
	success = 0
	for n in range(trials):
		d = random.randint(1, 20)
		if d >= i:
			success += 1
	print(success / trials)
