
# To convert any given number to given base form
def number_to_base(A ,B):
        if A==0:
            return 0
        result=''
        while A>0:
            rem=A%B
            A=A//B
            result+=str(rem)
        result=result[::-1]
        return result

print(number_to_base(5,2))  #101

print(number_to_base(357,7))  #1020

print(number_to_base(357,16))  #165
