'''The count-and-say sequence is the sequence 
of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.

Solution:
Try constructing the sequence starting from 1.

For constructing the current sequence, 
you need to look at the previous sequence and count the 
size of the contiguous sequences.
'''

def count_and_say(n): 
    
    # Base cases 
    if (n == 1): 
        return "1"
    if (n == 2): 
        return "11"
  
    # Find n'th term by generating all terms from 3 to n-1.  
    # Every term is generated using previous term 

    # Initialize previous term 
    s = "11" 

    for i in range(3, n+1): 
          
        # In below for loop, previous character is processed 
        # in current iteration.  
        # That is why  a dummy character is  
        # added to make sure that loop runs one extra iteration. 
        s += '$'
        l = len(s) 

        # Initialize count of matching chars
        cnt = 1 

        # Initialize i'th term in series    
        tmp = "" 

        # Process previous term to find the next term 

        for j in range(1 , l): 
              
            # If current character does't match 
            if (s[j] != s[j - 1]): 
                  
                # Append count of str[j-1] to temp 
                tmp += str(cnt + 0) 
  
                # Append str[j-1] 
                tmp += s[j - 1] 
  
                # Reset count 
                cnt = 1
              
    # If matches, then increment count of matching characters 
            else: 
                cnt += 1
  
        # Update str 
        s = tmp 
    return s

print(count_and_say(5))

