'''Given an array arr and a number K where K is smaller than size of array, 
   the task is to find the K’th smallest element in the given array. 
   It is given that all array elements are distinct.'''
#Time Complexity of this solution is O(nLogn).
#code
print("Enter Test Cases")
T=int(input())
while(T!=0):
	print("Enter the no. of elements")
	N=input()
	print("Enter the array elements")
	arr=list(map(int,input().split()))
	print("Enter the K")
	k=int(input())
	arr=sorted(arr)
	print(arr[k-1])
	T=T-1
print("Done")
