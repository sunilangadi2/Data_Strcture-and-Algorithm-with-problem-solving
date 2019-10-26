'''Consider an array of integers, . We define the absolute difference
 between two elements,  and  (where ), to be the absolute value of .

Given an array of integers, find and print the minimum 
absolute difference between any two elements in the array. 
For example, given the array  we can create  pairs of numbers:  
and . The absolute differences for these pairs are ,  and . 
The minimum absolute difference is .

Hacker Rank: Minimum Absolute Difference in an Array'''
# Greedy approach is to sort the array then just calculate 
# the least differnce

def minimumAbsoluteDifference(arr):
    
    arr=sorted(arr)

    return (min(abs(x-y) for x,y in zip(arr,arr[1:])))


if __name__ == '__main__':
    
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)

