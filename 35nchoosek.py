#35nchoosek.py by Khalid Saif Co authored with Natnael Tsegai

def factorial(n):								#Factorial function
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
	
def n_choose_k(n, k):
	if k < 0 or k > n or n < 0:
		return 0
	return factorial(n) / (factorial(k) * factorial(n - k))

print(n_choose_k(3, 2))
print(n_choose_k(21, 3))
print(n_choose_k(1, 2))
print(n_choose_k(0, 2))