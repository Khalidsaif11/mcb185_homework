# 38quiz.py Ethan Djou Coauthored: Khalid Saif, George Mo, Jordan S

def greg(n):
	sign = -1
	end = 0
	for x in range(0, n + 1):
		sign = sign * -1
		equation = (sign)/(2*x + 1)
		end = end + equation
	end = end * 4
	return(end)



def nila(n):
	n1 = 2
	pi = 3
	sign = 1
	for x in range(1, n + 1):
		n3 = n1 + 2
		n2 = n1 + 1
		mult = (n1 * n2 * n3)
		n1 = n3
		pi = pi + (sign * 4 / mult)
		sign = sign * -1
	return(pi)

def task(n):
	for x in range(90, n+1):
		print(nila(x), greg(x))
		
task(100)
