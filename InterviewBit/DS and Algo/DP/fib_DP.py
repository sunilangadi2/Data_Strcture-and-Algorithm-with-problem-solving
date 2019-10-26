""" Calculating nth fibonacci using dynamic programming"""
""" This is DP because solution once calculated used for the next"""

def fibonacci(n):
	F=[0,1]
	
	for i in range(2,n+1):
		r=F[i-1]+F[i-2]
		F.append(r)
	print("fibonacci series")
	print(F)
	print("Nth fibonacci")
	return F[n]

if __name__ == '__main__':
	n=int(input())
	
	print(fibonacci(n))
