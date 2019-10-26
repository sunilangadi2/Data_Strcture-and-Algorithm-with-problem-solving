''' Given 3 stacks if different height arrange the stacks and 
    return the length of stack which are same height''' 


h1=[3, 2, 1, 1, 1]
h2=[4, 3, 2]
h3=[1, 1, 4, 1]

def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    h1=h1[::-1]
    h2=h2[::-1]
    h3=h3[::-1]
    
    s1=[]
    s2=[]
    s3=[]
    sum1,sum2,sum3=0,0,0

    for n in h1:
        sum1+=n
        s1.append(sum1)
      

    for n in h2:
        sum2+=n
        s2.append(sum2)

    for n in h3:
        sum3+=n
        s3.append(sum3)

    s1=s1[::-1]
    s2=s2[::-1]
    s3=s3[::-1]

    
    m=min(s1,s2,s3 ,key =len)
    if m==s1:
        for n in s1:
            if n in s2 and n in s3:
                return n
    elif m==s2:
        for n in s2:
            if n in s1 and n in s3:
                return n         

    elif m==s3:
        for n in s3:
            if n in s2 and n in s1:
                return n

    # If not possible return 0
    return 0
print(equalStacks(h1,h2,h3))