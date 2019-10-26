'''
Given an array of integers, find the subset of non-adjacent elements 
with the maximum sum. Calculate the sum of that subset.

For example, given an array  we have the following possible subsets:

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8
Our maximum subset sum is 8.'''


'''
Idea: store solutions for problem of size i-2 and i-1, 
where i is the size of the subproblem. 
The solution for problem of size i is either solution 
for problem i-1, or solution for problem i-2, 
or solution of problem i-2 + arr[i], or ar[i]. Iterate for every i. 
Start with 0, 0 for problems of size - 2 and -1
'''
# TC- O(n)
# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    a,b = 0,0
    for val in arr:
        a,b = b, max(a, a + val, b, val) 
    return b

if __name__ == '__main__':
   
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(res)
