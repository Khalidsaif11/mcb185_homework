								# 20demo.py by Khalid Saif

import math

print('hello, again') 			# greetings

"""
This is a
multi-line
comment
"""

print(1.5e-2) 					#math operators try out
print(1+1)
print(1-1)
print(2*2)
print(1/2)
print(2**3)
print(5 // 2)
print(5 % 2)
print(5 * (2+1))

print(abs(-10))    				#math functions
print(pow(5, 2))
print(round(5.34387, ndigits=3))
print(math.ceil(5.5))
print(math.floor(5.5))
print(math.log(2.3))
print(math.log2(8))
print(math.log10(100))
print(math.sqrt(4))
print(math.pow(5, 2))
print(math.factorial(5))

print(math.e) 					#constants
print(math.pi)
print(math.inf)
print(math.nan)

print(0.1 * 3)

a = 3							# side of triangle
b = 4							# side of triangle
c = math.sqrt(a**2 + b**2)		# hypotenuse of triangle
print(c)

print(type(a), type(b), type(c))		# Type
print(type(a), type(b), type(c), sep=', ')

def greeting():					# making functions
	print('hello yourself')

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c
x = pythagoras(3, 4)
print(x)

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))
print(pythagoras(1, 1))


# PRACTICE 

def signchange(a):				#negative number into postive and vice versa.
	return -a
print(signchange(3))
print(signchange(-10))

def arearec(a, b):				#area rectangle
	return a*b
print(arearec(5, 2))

def areatriangle(b, h):			#area triangle
	return 0.5 * b * h
print(areatriangle(10, 2))

def circumference(r):			#circumference circle
	return 2 * math.pi * r
print(circumference(2))

def tempconvert(fahrenheit):	# temperature convertor
	celsius = (fahrenheit - 32) * 5/9
	return celsius
print(tempconvert(70))

def mph_to_kph(mph):			#mph to kph speed convert
	kph = mph * 1.60934
	return kph
print(mph_to_kph(80))

def dna_concentration(od260, dilution_factor):
	concentration = 50 * od260 * dilution_factor
	return concentration
print(dna_concentration(0.6, 50))

def distance(x1, y1, x2, y2):	#distance computation
	d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return d
print(distance(4, 3, 5, 4))

def midpoint(x1, y1, x2, y2):	#midpoint computation
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
print(midpoint(3, 6, 1, 2))


#String

s = 'hello world'
print(s, type(s))

#conditionals

a = 2							#Values chosen
b = 2
if a==b:
	print('a equals b')

if a==b:
	print('a equals b')
	print(a, b)

if a==b:
	print('a equals b')
print(a, b)

c = a==b						#boolean, true/false
print(c)
print(type(c))

if a < b:						#if elif else
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b')

if 		a < b: 	print('a < b')	#horizontally aligned
elif 	a > b: 	print('a > b')
else:			print('a == b')

if a < b or a > b: print('all things being equal, a and b are not')		#chaining
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3							#floating point
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')

print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'						#comparing strings
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')


#More practice 2

def isinteger(n):			#integer function
	if n == n // 1: return True
	else		  : return False
print(isinteger(5))				#integer
print(isinteger(4.1))			#not integer

def isodd(a):				#odd function
	if a % 2 != 0: return "odd"
	else		 : return "not odd"
print(isodd(5))
print(isodd(12))

def valid_probability(p):		#Valid probability
	if 0 <= p <= 1: return "valid"
	else		  : return "not valid"
print(valid_probability(5))
print(valid_probability(0.5))

def mw_dna_bases(nt):			#molecular weight of dna bases
	if nt == 'A': return 313.2
	if nt == 'C': return 289.2
	if nt == 'G': return 329.2
	if nt == 'T': return 304.2
	else 	    : return "not a dna base"
print(mw_dna_bases('G'))
print(mw_dna_bases('Z'))

def dna_complement(nt):
	if   nt == 'A': return 'T'
	elif nt == 'C': return 'G'
	elif nt == 'G': return 'C'
	elif nt == 'T': return 'A'
	else		  : return 'unknown nucleotide'
print(dna_complement('T'))
print(dna_complement('Z'))


a = 1							#testing unequal types
s = 'G'
if a < s: print('a < s')

def pythagoras(a, b):			#assertion tryout
	assert(a > 0)
	assert(b > 0)
	return math.sqrt(a**2 + b**2)
print(pythagoras(-1, 1))

def pythagoras(a, b):			#sys tryout
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)
