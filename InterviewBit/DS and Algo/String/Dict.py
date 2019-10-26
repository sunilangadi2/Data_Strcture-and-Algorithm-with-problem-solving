#Given a string write a function to check 
#is this permutation forms palindrome

def IsPFP(string):
    dic={}
    count=''
    for char in string:
        if not dic.get(char):
            dic[char]=dic.get(char,0)+1
        #count+=str(dic[char])
        else:
            dic[char]=dic.get(char,0)-1
    print(dic.values())
    for v in dic.values():
        print(v)
        if v>=2:
            return False
    return True

print(IsPFP('snil'))
