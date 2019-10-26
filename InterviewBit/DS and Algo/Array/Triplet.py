''' Given an array of distinct integers and a sum value. 
    Find count of triplets with sum smaller than given sum value. 
    Expected Time Complexity is O(n2).

    Input : arr[] = {-2, 0, 1, 3}
        sum = 2.
	Output : 2
	Explanation :  Below are triplets with sum less than 2
               (-2, 0, 1) and (-2, 0, 3) 

	Input : arr[] = {5, 1, 3, 4, 7}
	        sum = 12.
	Output : 4
	Explanation :  Below are triplets with sum less than 12
	               (1, 3, 4), (1, 3, 5), (1, 3, 7) and 
	               (1, 4, 5)

	Algorithm:
	1) Sort the input array in increasing order.
	2) Initialize result as 0.
	3) Run a loop from i = 0 to n-2.  An iteration of this loop finds all
   	   triplets with arr[i] as first element.
     a) Initialize other two elements as corner elements of subarray
        arr[i+1..n-1], i.e., j = i+1 and k = n-1
     b) Move j and k toward each other until they meet, i.e., while (j < k), 
     		then do k--
            // Else for current i and j, there can (k-j) possible triplets
            // that satisfy the constraint.
            (ii) Else Do ans += (k - j) followed by j++  '''

def count_triplet(arr,sume):
	arr=sorted(arr)
	n=len(arr)
	count=0

	for i in range(0,n-2):
		# Initialize other two elements as corner elements  
        # of subarray arr[j+1..k] 
		j,k = i+1,n-1

		# Use Meet in the Middle concept  
		while(j<k):

			# If sum of current triplet is more or equal,  
            # move right corner to look for smaller values 
			if arr[i]+arr[j]+arr[k]>=sume:
				k-=1
			# Else move left corner  
			else:
				# This is important. For current i and j, there  
                # can be total k-j triplets possible. 
				count+=(k-j)
				j+=1

	return count

print(count_triplet([5, 1, 3, 4, 7],15))
