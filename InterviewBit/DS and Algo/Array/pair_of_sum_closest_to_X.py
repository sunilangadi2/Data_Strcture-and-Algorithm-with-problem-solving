''' Given a sorted array and a number x, 
	find a pair in array whose sum is closest to x.
	Examples:

	Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
	Output: 22 and 30

	Input: arr[] = {1, 3, 4, 7, 10}, x = 15
	Output: 4 and 10

	Solution:
	1) Initialize a variable diff as infinite (Diff is used to store the 
   	   difference between pair and x).  We need to find the minimum diff.
	2) Initialize two index variables l and r in the given sorted array.
       (a) Initialize first to the leftmost index:  l = 0
       (b) Initialize second  the rightmost index:  r = n-1
	3) Loop while l < r.
       (a) If  abs(arr[l] + arr[r] - sum) < diff  then 
           update diff and result 
       (b) Else if(arr[l] + arr[r] <  sum )  then l++
       (c) Else r--
'''

def closest_sum(arr,x):
	diff=999
	n=len(arr)
	l,r,res_l,res_r=0,n-1,0,0
	while l<r:
		if(abs(arr[l]+arr[r]-x)<diff):
			diff=abs(arr[l]+arr[r]-x)
			res_l=l
			res_r=r
		if((arr[l]+arr[r]) < x):
			l+=1
		else:
			r-=1
	print("The closest pair sum is {} and {}".format(arr[res_l],arr[res_r]))

# Driver code to test above 
if __name__ == "__main__": 
    arr = [90, 85, 75, 60, 120, 150, 125]
    n = len(arr) 
    x=220
    closest_sum(arr, x) 
