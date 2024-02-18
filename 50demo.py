#50demo.py by Khalid Saif

seq = 'GAATTC'
print(seq[0], seq[1], seq[2], seq[3])#gives first, second, third characters.
print(seq[-1], seq[-2])									#start from last character from -1.


for nt in seq: print(nt, end='')						#put 'end' to keep horizontally.
print()

for i in range(len(seq)):
	print(i, seq[i])


s = 'ABCDEFGHIJ'
print(s[0:5])											#slice, end before limit.
print(s[0:8:2])											#initial, limit, increment.
print(s[0:5], s[:5])									#initial usually 0
print(s[5:len(s)], s[5:])								#start 5, end max length
print(s, s[::], s[::1], s[0:len(s)], s[::-1])			#all same! last is reverse
print(s[0], s[0:1])										#both give one character!


tax = ('Homo', 'sapiens', 9606)							#tuple
print(tax)

"""														#errors
s[0] = 'C'
tax[0] = 'human'
"""

print(tax[0])
print(tax[::-1])

def quadratic(a, b, c):									#return output is tuple!
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2


x1, x2 = quadratic(5, 6, 1)								# unpacked tuple - yes!
print(x1, x2)
intercepts = quadratic(5, 6, 1)							# packed tuple - no!
print(intercepts[0], intercepts[1])


nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
print()

for i, nt in enumerate(nts): #index and value in separate named variables.
	print(i, nt)										#enumerate
print()

names = ('adenine', 'cytosine', 'guanine', 'thymine')	#two containers parallel
for i in range(len(names)):
	print(nts[i], names[i])
print()


for nt, name in zip(nts, names):						#more neat parallel zip
	print(nt, name)
print()


for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
print()


nts = ['A', 'T', 'C']									#lists! uses square brackets.
print(nts)
nts[2] = 'G'											#mutable!
print(nts)

nts.append('C')											#can add elements
print(nts)												#with list only

last = nts.pop()										#remove elemnts from end
print(last)

nts.sort()												#sort & inverse sort
print(nts)
nts.sort(reverse=True)
print(nts)
print()

n = ['1', '5', '0.5']									#my example
n.sort(reverse=True)
print(n)
print()

nucleotides = nts										#change nts changes nucleotides
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
print()

"""
list.copy()	#to make copy. Not using!
"""

items = list()											#creat empty list then add
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)
print()

alph = 'ACDEFGHIKLMPQRSVW'								#string into list of letters
print(alph)
aas = list(alph)
print(aas)
print()


text = 'good day   to you'	#split into strings, use spaces
words = text.split()
print(words)


line = '1.41, 2.72, 3.14'
print(line.split(','))									#For TSV OR CSV, split using \t or comma
print()

s = '-'.join(aas)										#delimiter
print(s)
s = ''.join(aas)
print(s)
print()


if 'A' in alph: print('yay')							#use of 'in' with conditionals for searching
if 'a' in alph: print('no')

print('index G?', alph.index('G'))#use of 'index' to return index
#print('index Z?', alph.index('Z'))						#ERROR, if not found!


print('find G?', alph.find('G'))#use of 'find' strings only, for searching
print('find Z?', alph.find('Z'))						#not found, returns '-1'

#if thing in list: idx = list.index(thing)				#use 'in' for list & tuple


#PRACTICE PROBLEMS:

def minimum(vals):										#function to find min in a list
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
lis = ['5', '8', '3', '1', '0.5']
print(minimum(lis))


def minmax(vals):										#function to find min & max in list
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
lis = ['5', '8', '3', '1', '0.5']
print(minmax(lis))


def mean(vals):											#function to find mean in a list
	total = 0
	for val in vals: total += val
	return total / len(vals)							#len gives you the number of characters total
lis = [5, 8, 3, 1]
print(mean(lis))


import math
'''
def entropy(probs):										#Kullback-Leibler 
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5])
'''

def dkl(P, Q):											#Kullback-Leibler2
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))


'''
with open(path) as fp:									#files
	for line in fp:
	do_somethiing_with(line)


fp = open(path)											#alternate way
for line in fp:
	do_something_with(line)
fp.close()


import gzip												#read compressed files
with gzip.open(path, 'rt') as fp:						#same as gunzip -c path
	for line in fp:
		print(line, end='')
'''

i = int('42')											#convert types str to num
x = float('0.61803')
