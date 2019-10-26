''' Given a string, that contains special character together 
    with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), 
    reverse the string in a way that special characters are 
    not affected.

Examples:

Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.  
Only subsequence "abc" is reversed

Solution:
1) Let input string be 'str[]' and length of string be 'n'
2) l = 0, r = n-1
3) While l is smaller than r, do following
    a) If str[l] is not an alphabetic character, do l++
    b) Else If str[r] is not an alphabetic character, do r--
    c) Else swap str[l] and str[r]'''

def reverse_wos(s):
    n=len(s)
    l,r=0,n-1
    # strings are immutable changing char in string is not allowed
    LIST = list(c for c in s)  
    while l<r:
        if not s[l].isalpha():
            l+=1
        elif not s[r].isalpha():
            r-=1
        else:
            LIST[l], LIST[r] = LIST[r],LIST[l]
            l += 1
            r -= 1
  
    return ''.join(LIST)
  
# Utility functions to convert string to list for changing char
def toList(string): 
    List = [] 
    for i in string: 
        List.append(i) 
    return List

print("Enter string")
s=input()
print(reverse_wos(s))
print(reverse_wos("S*n$i@lj"))
