'''
# Sample code to perform I/O:

name = input()         		 # Reading input from STDIN
print('Hi, %s.' % name)		 # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

def solve (Q): #takes query input and processes them
    # your code ()
    arr=[]
    while Q:
        I=input().split()
        if I[0]=='A':
            arr.append(int(I[1]))
        elif I[0]=='I':
            for i in range(0,len(arr)):
                arr[i]+=int(I[1])
        elif I[0]=='D':
            for i in range(0,len(arr)):
                arr[i]-=int(I[1])
        else:
            arr=sorted(arr,reverse=True)
            i=int(I[1])
            print(arr[i-1])
        Q=Q-1 


noOfTestCasesQ = int(input())

while(noOfTestCasesQ > 0):
    noOfQueriesP = int(input())
    solve(noOfQueriesP)
    noOfTestCasesQ = noOfTestCasesQ - 1