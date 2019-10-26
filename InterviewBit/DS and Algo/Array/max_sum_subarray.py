'''Given anarray find maximum sum of subarray from the given array '''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxsum = cursum = A[0]
        for a in A[1:]:
            cursum = max(cursum + a, a)
            maxsum = max(cursum, maxsum)
        return maxsum
    
s=Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  #6

print(s.maxSubArray([-9,4,5,6,-10,3,5,6,7,-23]))  #26
