'''
Given an array A of integers, find the index of values 
that satisfy A + B = C + D, where A,B,C & D are integers 
values in the array
'''
from collections import OrderedDict
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def equal(self, A):
	    d = OrderedDict()
	    for i in range(len(A)):
	        for j in range(i+1,len(A)):
	            ans = A[i]+A[j]
	            if(ans in d):
	                if(i not in d[ans] and j not in d[ans]):
	                    d[ans].append(i)
	                    d[ans].append(j)
	            else:
	                d[ans] = [i,j]
	    print(d)
	    for k in d:
	        if(len(d[k])>2):
	            return d[k][0:4]
	    return []

s=Solution()
print(s.equal([3,4,7,1,2,9,8]))