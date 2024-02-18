#53genometats.py by Khalid Saif

import gzip
import sys
import math


gffpath = sys.argv[1]
feature = sys.argv[2]
lengths = []

with gzip.open(gffpath, 'rt') as file: #path to the GFF
	for line in file:					#and and the type of feature
		word = line.split('\t')
		if word[2] == feature:
			begin = int(word[3])
			end = int(word[4])
			lengths.append(end - begin + 1)
			count = len(lengths)

def mean(lengths):								#mean function
	total = 0
	for i in lengths:
		total += i
	if len(lengths) > 0:
		return total / len(lengths)
mean = mean(lengths)

def sd(lengths, mean):							#standard deviation function
	diff = 0
	for i in lengths:
		diff += (i - mean)**2
	if len(lengths) > 0:
		return math.sqrt(diff / len(lengths))
sd = sd(lengths, mean)

def median(lengths):							#median function
	lengths.sort()
	val = len(lengths)
	if val % 2 == 0:
		n = (lengths[val//2 - 1] + lengths[val//2])// 2		#even
		return n
	else:
		return lengths[val // 2]				#odd
median = median(lengths)

def minimum(lengths):							#minimum function
	mini = lengths[0]
	for value in lengths[1:]:
		if value < mini:
			mini = value
	return mini
minimum = minimum(lengths)

def maximum(lengths):							#maximum function
	maxi = lengths[0]
	for value in lengths[1:]:
		if value > maxi:
			maxi = value
	return maxi
maximum = maximum(lengths)


print(f'count  is {count}')
print(f'min    is {minimum}')
print(f'max    is {maximum}')
print(f'mean   is {math.ceil(mean)}')
print(f'sd     is {math.floor(sd)}')
print(f'median is {median}')