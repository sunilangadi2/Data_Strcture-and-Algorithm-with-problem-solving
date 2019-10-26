def IsPermutation(s1,s2):
    if len(s1)!=len(s2):
        return False
    else :
        return sorted(s1)==sorted(s2)


print(IsPermutation('slinu','sunil'))  # Time complexity=O(nlogn)
