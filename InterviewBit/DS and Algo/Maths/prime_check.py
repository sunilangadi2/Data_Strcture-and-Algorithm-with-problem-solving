'''program to check if the number is prime or not.

Definition: A prime number is a natural number greater than 1 
that has no positive divisors other than 1 and itself. 
The first few prime numbers are {2, 3, 5, 7, 11, ….}.

Solution:The idea to solve this problem is to iterate through 
all the numbers starting from 2 to (N/2) using a for loop and 
for every number check if it divides N. 
If we find any number that divides, we return false. 
If we did not find any number between 2 and N/2 which divides N then 
it means that N is prime and we will return True.'''

# Python program to check if 
# given number is prime or not 

num = 10

# If given number is greater than 1 
if num > 1: 
	
	# Iterate from 2 to n / 2 
	for i in range(2, num//2): 
			
		# If num is divisible by any number between 
		# 2 and n / 2, it is not prime 
		if (num % i) == 0: 
			print(num, "is not a prime number") 
			break
	else: 
		print(num, "is a prime number") 

else: 
	print(num, "is not a prime number") 
