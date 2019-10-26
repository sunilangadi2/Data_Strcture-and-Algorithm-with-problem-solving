'''An element in a sorted array can be found in O(log n) time via binary search.
   But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. 
   So for instance, 1 2 3 4 5 might become 3 4 5 1 2.'''

'''1) Find middle point mid = (l + h)/2
   2) If key is present at middle point, return mid.
   3) Else If arr[l..mid] is sorted
    a) If key to be searched lies in range from arr[l]
       to arr[mid], recur for arr[l..mid].
    b) Else recur for arr[mid+1..r]
   4) Else (arr[mid+1..r] must be sorted)
    a) If key to be searched lies in range from arr[mid+1]
       to arr[r], recur for arr[mid+1..r].
    b) Else recur for arr[l..mid] 

    Time Complexity O(logn).'''

# Search an element in sorted and rotated array using 
# single pass of Binary Search 

# Returns index of key in arr[l..h] if key is present, 
# otherwise returns -1 
def search (arr, l, h, key): 
  if l > h: 
    return -1
  
  mid = (l + h) // 2
  if arr[mid] == key: 
    return mid 

  # If arr[l...mid] is sorted 
  if arr[l] <= arr[mid]: 

    # As this subarray is sorted, we can quickly 
    # check if key lies in half or other half 
    if key >= arr[l] and key <= arr[mid]: 
      return search(arr, l, mid-1, key) 
    return search(arr, mid+1, h, key) 

  # If arr[l..mid] is not sorted, then arr[mid... r] 
  # must be sorted 
  if key >= arr[mid] and key <= arr[h]: 
    return search(arr, mid+1, h, key) 
  return search(arr, l, mid-1, key) 

# Driver program 
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
key = 0
i = search(arr, 0, len(arr)-1, key) 
if i != -1: 
  print ("Index: %d"%i) 
else: 
  print ("Key not found") 

