''' Given an array of integers, write a function that returns true 
    if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.
    Example:

    Input: arr[] = {3, 1, 4, 6, 5}
    Output: True
    There is a Pythagorean triplet (3, 4, 5).

    Input: arr[] = {10, 4, 6, 12, 5}
    Output: False
    There is no Pythagorean triplet.

    Solution:

    Method 1 (Naive)
    A simple solution is to run three loops, three loops pick three array elements 
    and check if current three elements form a Pythagorean Triplet.
    TC is O(n^3)

    Method 2 (Use Sorting)
    We can solve this in O(n2) time by sorting the array first.

    1) Do square of every element in input array. This step takes O(n) time.

    2) Sort the squared array in increasing order. This step takes O(nLogn) time.

    3) To find a triplet (a, b, c) such that a2 = b2 + c2, do following.

    Fix ‘a’ as last element of sorted array.
    Now search for pair (b, c) in subarray between first element and ‘a’. 
    A pair (b, c) with given sum can be found in O(n) time 
    using meet in middle algorithm discussed in method 1 of this post.
    If no pair found for current ‘a’, then move ‘a’ 
    one position back and repeat step 3.2.'''
    
# Returns true if there is Pythagorean triplet in ar[0..n-1] 

def is_pythagorean_triplet(arr):
    # Form the square of elements first
    arr=[n**2 for n in arr]

    arr=sorted(arr)
    # Fix the element a as last element a as i
    for i in range(len(arr)-1,1,-1):
        # other two elements are the corner of the elements
        j=0  # b as j
        k=i-1 # c as k
        while(j<k):
            # if triplet found
            if arr[j]+arr[k]==arr[i]:
                return True
            elif arr[j]+arr[k]>arr[i]:
                k-=1
            else:
                j+=1
    return False

print(is_pythagorean_triplet([3, 1, 4, 6, 5]))
