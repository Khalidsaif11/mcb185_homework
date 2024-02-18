#56birthday.py by Khalid Saif

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

total_shared_bd = 0
for a in range(trials):
	birthdays = []
	for b in range(people):
		r = random.randint(0, days - 1)
		birthdays.append(r)
	shared_bd = False
	for i in range(len(birthdays)):
		for j in range((i+1), len(birthdays)):
			if birthdays[i] == birthdays[j]:
				shared_bd = True
				break
	if shared_bd: total_shared_bd += 1
p = total_shared_bd / trials * 100
print(p)






'''
shared_bd = 0
for a in range(trials):
	birthdays = []
	for b in range(people):
		r = random.randint(1, days)
		birthdays.append(r)
		for i in range(people):
			for j in range((i+1), people):
				if birthdays[i] == birthdays[j]:
					shared_bd += 1
					break
p = shared_bd / trials
print(p)
'''