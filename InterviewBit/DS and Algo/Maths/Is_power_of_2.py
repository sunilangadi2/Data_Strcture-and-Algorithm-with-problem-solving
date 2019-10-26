''' Find if Given number is power of 2 or not. 
	More specifically, find if given number can be expressed as 2^k where k >= 1.

	return 1 if the number is a power of 2 else return 0'''

def power(A):
        x = int(A)
        if x>1 and x & x-1 == 0 :
        	#v = x & x-1
        	#print(v)
            return 1
        return 0

def check_power(A):
        
        A=int(A)
        if A==1:
            return 0
        # go on dividing by 2 untill A becomes less than 2
        while A!=1 and A%2==0:
            A=A//2
        if A==1:
            return 1
        else:
            return 0


print(power(16))
print(check_power(15))
print(check_power(128))