#44randompi.py by Khalid Saif

import math
import random

inside_circle = 0
total_points = 0
while True:
	x = random.random()
	y = random.random()
	d = math.sqrt(x**2 + y**2)							#distance
	if d < 1: inside_circle += 1
	total_points += 1
	pi = 4* (inside_circle / total_points)
	print(pi)											#^c to break 