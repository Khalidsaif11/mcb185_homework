# 21quadratic.py by Khalid Saif

import math

def quadratic_formula(a, b, c):			#quadratic formula
	assert(b**2 - 4*a*c > 0)
	x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
	x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
	return x1, x2
print(quadratic_formula(4, 16, 5))
print(quadratic_formula(8, 30, 11))
print(quadratic_formula(10, 2, 5))		#negative under root tryout


x1, x2 = quadratic_formula(10, 12, 11)