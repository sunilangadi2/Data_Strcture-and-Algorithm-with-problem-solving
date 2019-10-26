'''Bubble Sort is the simplest sorting algorithm that 
works by repeatedly swapping the adjacent elements if they are in wrong order.
Example:
First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Optimized Implementation:
The above function always runs O(n^2) time even if the array is sorted.
It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.

'''

def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    print(arr)


# An optimized version of Bubble Sort 
def bubbleSort(arr): 
    n = len(arr) 
   
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break
    return arr

bubblesort([3,2,4,5,1])
print(bubbleSort([3,2,4,5,1]))





