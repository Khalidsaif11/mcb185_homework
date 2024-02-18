#55colorname.py by Khalid Saif

import sys 
import gzip

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

maxi = 1000
with open(colorfile) as fp:
	for line in fp:
		words = line.split('\t')
		color = words[0]
		color_name_value = words[2]
		value = color_name_value.split(',')
		r = int(value[0])
		g = int(value[1])
		b = int(value[2])
		d = abs(R-r) + abs(G-g) + abs(B-b)
		if d < maxi:
			maxi = d
			result = color
print(result)