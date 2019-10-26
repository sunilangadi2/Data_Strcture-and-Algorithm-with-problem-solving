'''Given a string, determine if it is a palindrome, 
    considering only alphanumeric characters and ignoring cases.

    Example:

    "A man, a plan, a canal: Panama" is a palindrome.

    "race a car" is not a palindrome.

    Return 0 / 1 ( 0 for false, 1 for true ) for this problem'''

    
    # @param A : string
    # @return an integer
def isPalindrome(A):
        end = len(A) - 1
        start = 0
        if not A:
            return 1
        while start<end:
            if A[start].isalnum() and A[end].isalnum():
                if A[start].lower() != A[end].lower():
                    return 0
                else:
                    start+=1
                    end-=1
            elif not A[start].isalnum():
                start+=1
            elif not A[end].isalnum():
                end-=1
            
        return 1

# We can check given string is palindrome or not just by reversing the string itself
def isPalindrome_Eff(A):
    A = A.lower().replace(" ", "").replace("-", "").replace(",", "").replace(":", "").replace(";", "").replace("'", "").replace('"', '')
    return int(A == A[::-1])    


print(isPalindrome("A man, a plan, a canal: Panama"))

print(isPalindrome_Eff("A cman, a plan, a canal: Panama"))