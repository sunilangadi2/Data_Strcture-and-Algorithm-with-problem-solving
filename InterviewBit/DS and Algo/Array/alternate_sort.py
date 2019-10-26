'''Given two sorted arrays A and B, generate all possible arrays such that 
   first element is taken from A then from B then from A and 
   so on in increasing order till the arrays exhausted. 
   The generated arrays should end with an element from B.

    For Example 
    A = {10, 15, 25}
    B = {1, 5, 20, 30}

    The resulting arrays are:
      10 20
      10 20 25 30
      10 30
      15 20
      15 20 25 30
      15 30
      25 30  '''

# A utility function to print an array 
def printArr(arr,n): 
  
    for i in range(n): 
        print(arr[i] , " ",end="") 
    print() 
   
''' Function to generates and prints all 
    sorted arrays from alternate elements of 
   'A[i..m-1]' and 'B[j..n-1]' 
   If 'flag' is true, then current element 
   is to be included from A otherwise 
   from B. 
   'len' is the index in output array C[]. 
    We print output  array  each time 
   before including a character from A 
   only if length of output array is 
   greater than 0. We try than all possible combinations '''
def generateUtil(A,B,C,i,j,m,n,len,flag): 
  
    if (flag): # Include valid element from A 
      
        # Print output if there is at 
        # least one 'B' in output array 'C' 
        if (len): 
            printArr(C, len+1) 
   
        # Recur for all elements of 
        # A after current index 
        for k in range(i,m): 
          
            if ( not len): 
              
                ''' this block works for the 
                    very first call to include 
                    the first element in the output array '''
                C[len] = A[k] 
   
                # don't increment lem 
                # as B is included yet 
                generateUtil(A, B, C, k+1, j, m, n, len,  not flag) 
              
            else:   
    
                # include valid element from A and recur  
                if (A[k] > C[len]): 
                  
                    C[len+1] = A[k] 
                    generateUtil(A, B, C, k+1, j, m, n, len+1, not flag)     
    else:   
    
        # Include valid element from B and recur 
        for l in range(j,n): 
          
            if (B[l] > C[len]): 
              
                C[len+1] = B[l] 
                generateUtil(A, B, C, i, l+1, m, n, len+1, not flag) 
              
  
# Wrapper function  
def generate(A,B):
    m=len(A)
    n=len(B) 
    #output array
    C=[]  
    for i in range(m+n+1): 
        C.append(0) 
    generateUtil(A, B, C, 0, 0, m, n, 0, True) 
   

generate([10,15,25],[1,5,20,30])