from collections import Counter
"""Given a string, check if it is a permutation of a palindrome."""
# Logic is in plindrome other than one letter rest all appears more than once 
# But this logic does not work for palindrome check
def is_palindrome_permutation(data):  
    data = Counter(data.replace(' ', '').lower())
    print(data)
    return sum(freq%2 for freq in data.values()) < 2

print(is_palindrome_permutation('abaacccaacba'))
