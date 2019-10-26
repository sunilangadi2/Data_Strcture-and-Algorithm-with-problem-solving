# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:41:32 2018

@author: Sunil Angadi
"""

""" Return list with all palindrome strings within text.

    The base of this algorithm is to start with a given character,
    and then see if the surrounding characters are equal. If they
    are equal then it's a palindrome and is added to results set,
    extend to check if the next character on either side is equal, 
    adding to set if equal, and breaking out of loop if not.

    This needs to be repeated twice, once for palindromes of 
    odd lengths, and once for palindromes of an even length."""
    

def all_palindromes(text):
    
    results = set()
    text_length = len(text)
    for idx, char in enumerate(text):

        # Check for longest odd palindrome(s)
        start, end = idx - 1, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            results.add(text[start:end+1])
            start -= 1
            end += 1

        # Check for longest even palindrome(s)
        start, end = idx, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            results.add(text[start:end+1])
            start -= 1
            end += 1

    return list(results),max(results,key=len)


def palindromes(text):
    text = text.lower()
    results = []

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]
# Checking this chunk is palindrome or not just by reversing the chunk itself
            if chunk == chunk[::-1]:
                results.append(chunk)
    if results:
    	return max(results, key=len), results
    else:
    	return text[0]

if __name__=='__main__':
    text="abbcccbbbcaaccbababcbcabca"
    # * to unpack the arguments in the list
    print(*all_palindromes(text),sep='\n')
    print(palindromes("abbcccbbbcaaccbababcbcabca"))
    print(palindromes("ca"))
    print(palindromes("LiriL"))
    print(all_palindromes("aaaa"))
    print(len("aaaa")+len(all_palindromes("aaaa"))-1)