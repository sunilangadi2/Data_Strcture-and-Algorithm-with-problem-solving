# -*- coding: utf-8 -*-
"""
Created on Sat May 19 14:30:19 2018

@author: Sunil Angadi
"""

""" Heap Sort Algorithm for sorting in increasing order:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. 
   Replace it with the last item of the heap followed by reducing the size of heap by 1. 
   Finally, heapify the root of tree.
3. Repeat above steps while size of heap is greater than 1.

Time Complexity-nlogn for all cases """

# To heapify the subtree rooted at index i
def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
   # To identify which child as largest either left or right
    if(l<n and arr[l]>arr[largest]):
        largest=l
    if(r<n and arr[r]>arr[largest]):
        largest=r
    # Replace the largest child as the root of the subtree then recursively heapify it.    
    if(largest!=i):
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)
        
def heapsort(arr):
    n=len(arr)
    for i in range(n//2 -1,-1,-1):
        heapify(arr,n,i)  # To build max heap
    # One by one extract the elements from the root and sort it
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

# Driver code to test above
if __name__=='__main__':
    arr = [ 12, 11, 13, 5, 6, 7,3,4,1]
    heapsort(arr)
    n = len(arr)
    print ("Sorted array is")
    for i in range(n):
        print("%d" % arr[i])
    
