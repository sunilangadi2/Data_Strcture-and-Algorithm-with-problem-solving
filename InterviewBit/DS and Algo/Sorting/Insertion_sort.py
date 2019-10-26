''' Insertion sort is a simple sorting algorithm that works 
    the way we sort playing cards in our hands.
	Time Complexity: O(n*2)
	Auxiliary Space: O(1)
'''

    # Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j=j-1
        arr[j+1] = key
        
    return  arr
# Driver code to test above 
arr = [12, 11, 13, 5, 6] 
print(insertionSort(arr))
