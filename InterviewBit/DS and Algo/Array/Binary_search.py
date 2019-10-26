# -*- coding: utf-8 -*-
"""
Created on Sat May 19 14:59:11 2018

@author: Sunil Angadi
"""
""" Binary Search: Search a sorted array by repeatedly 
    dividing the search interval in half.
 	Begin with an interval covering the whole array. 
 	If the value of the search key is less than the item in the middle of the interval,
 	narrow the interval to the lower half. Otherwise narrow it to the upper half. 
 	Repeatedly check until the value is found or the interval is empty.
 
 	Time complexity- logn for all cases """

def binary_search(arr,start,end,key):
    if end>=start:
        mid=(start+end)//2
        if(key==arr[mid]):
            return mid
        elif(key > arr[mid]):
            return binary_search(arr,mid+1,end,key)
        else:
            return binary_search(arr,start,mid-1,key)
    else:
        return -1


# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    while l <= r: 
        mid = (l + r) //2; 
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
    # If we reach here, then the element 
    # was not present 
    return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index %d "% result) 
else: 
    print("Element is not present in array")



if __name__=='__main__':
    arr=[10,23,45,67,89,98]
    n=len(arr)
    result=binary_search(arr,0,n-1,98)
    if result != -1:
        print("Element found")
    else:
        print("Element is not present in array")
