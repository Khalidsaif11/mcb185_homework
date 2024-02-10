#45dndstats.py by Khalid Saif co-authored with Ethan Djou & George Mo

import random

rolls = 10000

total_points = 0
for i in range(rolls):								#rolling  3D6
	score = 0
	d1 = random.randint(1, 6) 
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	score = d1 + d2 + d3
	total_points += score
average_3d6 = total_points / rolls
print('3D6\t', average_3d6)


total_points = 0
for i in range(rolls):								# 3D6r1 reroll ones	
	score = 0
	d1 = random.randint(1, 6) 
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	if d1 == 1: d1 = random.randint(1, 6)
	if d2 == 1: d2 = random.randint(1, 6)
	if d3 == 1: d3 = random.randint(1, 6)
	score = d1 + d2 + d3
	total_points += score
average_3d6r1 = total_points / rolls
print('3D6r1\t', average_3d6r1)


total_points = 0
for i in range(rolls):							# 3D6x2 pairs maximum
	score = 0
	for n in range(3):
		d1 = random.randint(1, 6) 
		d2 = random.randint(1, 6)
		if d1 > d2: score += d1
		else: score += d2
	total_points += score
average_3d6x2 = total_points / rolls
print('3D6x2\t', average_3d6x2)


total_points = 0
for i in range(rolls):							#drop lowest
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if   d1 <= d2 and d1 <= d3 and d1 <= d4: score += d2 + d3 + d4
	elif d2 <= d1 and d2 <= d3 and d2 <= d4: score += d1 + d3 + d4
	elif d3 <= d1 and d3 <= d2 and d3 <= d4: score += d1 + d2 + d4
	elif d4 <= d1 and d4 <= d2 and d4 <= d3: score += d1 + d2 + d3
	total_points += score
average_4d6d1 = total_points / rolls
print('4D6d1\t', average_4d6d1)