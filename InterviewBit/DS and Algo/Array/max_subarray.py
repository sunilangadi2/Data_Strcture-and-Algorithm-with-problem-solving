'''Find out the maximum sub-array of non negative numbers 
    from an array.
   The sub-array should be continuous. 
   That is, a sub-array created by choosing the second and 
   fourth element and skipping the third element is invalid.

    Maximum sub-array is defined in terms of the sum of the elements
    in the sub-array. 
    Sub-array A is greater than sub-array B if sum(A) > sum(B).

    Example:

    A : [1, 2, 5, -7, 2, 3]
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3]
    NOTE: If there is a tie, then compare with segment's length and
          return segment which has maximum length
    NOTE 2: If there is still a tie, then return the segment 
    with minimum starting index
'''
# Logic : approaching brute force only but keep tracking with more variables
def maxset(A):
        maxsumlist = []
        cursumlist = []
        maxsum = 0
        currsum = 0
        for i in A:
            if (i >= 0):
                currsum = currsum + i
                cursumlist.append(i)
                if(currsum > maxsum):
                    maxsum = currsum
                    maxsumlist = cursumlist
                elif(currsum == maxsum):
                    if(len(cursumlist) > len(maxsumlist)):
                        maxsumlist = cursumlist             
            elif(i<0):
                currsum = 0
                cursumlist = []
                    
        return maxsumlist,maxsum

print(maxset([-2,1,-3,4,2,1,-5,4]))  #6

print(maxset([14, 12, 11, 20]))

print(maxset([-9,4,5,6,-10,3,5,6,7,-23]))  #26
                        

