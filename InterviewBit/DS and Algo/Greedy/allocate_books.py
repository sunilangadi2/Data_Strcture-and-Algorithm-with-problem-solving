'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output 
  will cause the test cases to fail
'''

def solve (nArr, N, I, Q):
	# write your code here, which processes the passed variables, accepts queries and produces result.
	for i in range(Q):
		q=int(input())
		start=I
		sum_r=0
		sum_f=0
		for r in range(start,N):
			sum_r+=nArr[r]
			if r<N-1:
				sum_f=sum_r+nArr[r+1]
			while (sum_r<=q):
				sum_r+=nArr[r+1]
				start=r+1
				break
			elif (sum_f<=q):
				print(r+1)
				start=r+2
				break
			elif(r==N):
				print(-1)
				break

	
T = int(input()) #Total Testcases
while(T > 0):
	temp = [int(x) for x in input().split()]
	N, I, Q = temp[0], temp[1], temp[2]
	nArr = [int(x) for x in input().split()]
	solve(nArr, N, I, Q)
	T = T - 1