'''Merge Sort is a Divide and Conquer algorithm. 
It divides input array in two halves, calls itself for the two halves 
and then merges the two sorted halves. The merge() function is used for merging two halves.

Time Complexity: Sorting arrays on different machines. 
Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.
T(n) = 2T(n/2) +  Theta(n)
The above recurrence can be solved either using Recurrence Tree method or Master method. 
It falls in case II of Master Method and solution of the recurrence is Theta(nLogn).
Time complexity of Merge Sort is Theta(nLogn) in all 3 cases (worst, average and best) 
as merge sort always divides the array in two halves and take linear time to merge two halves.

Auxiliary Space: O(n)'''

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return arr
    
print(mergeSort([3,2,4,5,1]))
