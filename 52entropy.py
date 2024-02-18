#52entropy.py by Khalid Saif

import sys
import math

probs = []									#data from command line to program!
for arg in sys.argv[1:]:					#skip 0 name of program 52entropy.py
	f = float(arg)
	assert(f > 0 and f < 1)					#assert
	probs.append(float(arg))

total = 0
for p in probs: total += p
if not math.isclose(total, 1.0):			#sum to one or close
	sys.exit('error: probs must sum to 1.0') #error

h = 0
for p in probs:
	h -= p * math.log2(p)					#Shannon entropy formula

print(h)

'''
python3 52entropy.py 0.5 0.5
python3 52entropy.py 0.25 0.25 0.25 0.25
python3 52entropy.py 0.4 0.3 0.2 0.1
python3 52entropy.py 0.5 0.6
python3 52entropy.py 0.5 -1
'''