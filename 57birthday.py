#57birthday.py by Khalid Saif

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

total_shared_bd = 0
for a in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)
	shared_bd = False
	for j in range(people):
		day = random.randint(0, days - 1)
		calendar[day] += 1
		if calendar[day] == 2:
			shared_bd = True
			break
	if shared_bd: total_shared_bd += 1
p = total_shared_bd / trials * 100
print(p)





















'''
calendar = []
total_shared_bd = 0
for i in range(days):
	calendar.append(0)
shared_bd = False
for j in range(people):
	day = random.randint(1, days)
	calendar[day] += 1
	if calendar[day] >= 2:
		shared_bd = True#print('found')
		break
if shared_bd: total_shared_bd += 1
p = total_shared_bd / trials
print(p)
'''