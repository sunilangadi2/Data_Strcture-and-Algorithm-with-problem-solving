''' Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.'''

def firstMissingPositive(A):
        ns=set(A)
        print(ns)
        n=len(ns)+1
        for i in range(1,n):
            if i not in ns:
                return i
        return i+1 # case where list of 4 elements with [1...4] next is 5
      

print(firstMissingPositive([3,4,-1,1,1,2,2,3]))
