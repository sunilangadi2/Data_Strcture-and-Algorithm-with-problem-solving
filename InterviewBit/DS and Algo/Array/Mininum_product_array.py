'''Given an array a, we have to find minimum product possible 
	with the subset of elements present in the array. 
   The minimum product can be single element also.

Examples:

Input : a[] = { -1, -1, -2, 4, 3 }
Output : -24
Explanation : Minimum product will be ( -2 * -1 * -1 * 4 * 3 ) = -24

Input : a[] = { -1, 0 }
Output : -1
Explanation : -1(single element) is minimum product possible
 
Input : a[] = { 0, 0, 0 }
Output : 0

solution:
A simple solution is to generate all subsets, 
find product of every subset and return maximum product.

A better solution is to use the below facts.

1)If there are even number of negative numbers and no zeros, 
  the result is the product of all except the largest valued negative number.
2)If there are an odd number of negative numbers and no zeros, 
	the result is simply the product of all.
3)If there are zeros and positive, no negative, the result is 0. 
  The exceptional case is when there is no negative number and 
  all other elements positive then our result should be the 
  first minimum positive number.

Time Complexity : O(n)
Auxiliary Space : O(1)'''

# Python3 program to find maximum 
# product of a subset. 

# def to find minimum
# product of a subset 
def minProductSubset(a, n) :	 
	if (n == 1) : 
		return a[0] 

	# Find count of negative numbers, 
	# count of zeros, maximum valued 
	# negative number, minimum valued 
	# positive number and product 
	# of non-zero numbers 
	max_neg = float('-inf') 
	min_pos = float('inf') 
	count_neg = 0
	count_zero = 0
	prod = 1
	for i in range(0,n) : 

		# If number is 0, we don't 
		# multiply it with product. 
		if (a[i] == 0) :	 
			count_zero = count_zero + 1
			continue

		# Count negatives and keep 
		# track of maximum valued 
		# negative. 
		if (a[i] < 0) :	 
			count_neg = count_neg + 1
			max_neg = max(max_neg, a[i]) 
		
		# Track minimum positive 
		# number of array 
		if (a[i] > 0) : 
			min_pos = min(min_pos, a[i]) 

		prod = prod * a[i] 
	

	# If there are all zeros 
	# or no negative number 
	# present 
	if (count_zero == n or (count_neg == 0
					and count_zero > 0)) : 
		return 0

	# If there are all positive 
	if (count_neg == 0) : 
		return min_pos 

	# If there are even number of 
	# negative numbers and count_neg 
	# not 0 
	if ((count_neg & 1) == 0 and
					count_neg != 0) : 

		# Otherwise result is product of 
		# all non-zeros divided by 
		# maximum valued negative. 
		prod = int(prod / max_neg) 

	return prod; 

# Driver code 
a = [ 1, 1, 2, 4, 3,0 ,-6] 
n = len(a) 
print (minProductSubset(a, n))
