#43randomdna.py by Khalid Saif

import random

for n in range(3):
	print(f'>seq-{n+1}')
	for i in range(random.randint(10, 50)):
		print(random.choice('ACGT'), end='')
	print()