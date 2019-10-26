''' Print GCD and LCM of two numbers'''
''' If problem wants more than two then 
    just do two first using the result 
    proceed with third and repeat the same'''

def gcd(a,b):
	# using eucledian theorm
	return b if a%b==0 else gcd(b,a%b)

def lcm(a,b):
	result=gcd(a,b)
	# product of two numbers equal to product gcd and lcm
	return (a*b)//result  

def GCD(a,b):
	m=a
	n=b
	while(m!=n):
		if m>n:
			m=m-n
		else:
			n=n-m
	return n


# gcd for array of n numbers
arr=[2,4,6,8,10]
result=gcd(arr[0],arr[1])
for i in range(2,len(arr)):
	result=gcd(result,arr[i])
print(result)

print(GCD(16,4))
print(gcd(16,4))
print(lcm(15,4))