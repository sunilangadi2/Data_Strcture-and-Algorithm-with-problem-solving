# to print no of vowels in string
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

print(getCount("sunil angadi"))


# to replace ACGT with ACGU
def DNAtoRNA(dna):
    #return "".join([{"A": "A", "C": "C", "G": "G", "T": "U"}[b]for b in dna])
    return dna.replace('T','U')

print(DNAtoRNA("ACCAGTGA"))


# to return maximum product within an array of two adjacent elements 
def adjacent_element_product(array):
    return max( a*b for a, b in zip(array, array[1:]) )

print(adjacent_element_product([2,4,9,6,8]))


# to return an array of elements by using prod usage
def product_array(numbers):
    p=1
    for n in numbers:
        p*=n
    print(p)
    return [int(p) // int(i) for i in numbers]

print(product_array([2,4,6,8]))


# to return a string which contains 0 at the odd places and 1 at the even places
def stringy(size):
    s = ""
    for x in range (0, size):
        s+= str("1") if x%2 == 0 else str("0")
    return s

print(stringy(5))


# to return maximum element which has difference in the list
def max_gap(numbers):
    lst = sorted(numbers)
    return max(b-a for a,b in zip(lst, lst[1:]))

print(max_gap([2,4,6,1,7,3,10]))


# to return first non-repeating letter from string
def first_non_repeating_letter(string):
    string=string.lower()
    singles = [i for i in string if string.count(i) == 1]
    return singles[0] if singles else ''

print(first_non_repeating_letter('Pythonp'))


# to reverse a given number
def reverseNumber(n):
    if n < 0: return -reverseNumber(-n)
    return int(str(n)[::-1])

print(reverseNumber(-123))

# check wheather given string is palindrome or not
def balanced_num(n):
    s = str(n)
    l = (len(s)-1)//2
    same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
    return "Balanced" if same else "Not Balanced"

print(balanced_num(1234554321))

# to remove first and last char in a string
def remove_char(s):
    return s[1 : -1]

print(remove_char('ego'))


# given string of words return longest word
def longest_word(string_of_words):
    return max(string_of_words.split(), key=len)

print(longest_word('sunil angadi favourite is python'))


# To remove char in given string according to alphabetical 
# order till k times
def solve(st,k): 
    for l in sorted(st)[:k]:
        st=st.replace(l,'',1)
    return st

print(solve('google',3))


# Return unique sorted list of string which list1 strings are substrings of list2 strings.
def sub_string(a1, a2):
    return ({sub for sub in a1 if any(sub in s for s in a2)})

print(sub_string('sunil angadi','sun an'))


# Replace particular char in string with n times
def remove(s, n):
    return s.replace("l", "", n)

print(remove('Jealousy',2))

# Using Dictionary count the number of times each letter appears in a string 
def numericals(s):
    dictio = {}
    t = ""
    for i in s:
        dictio[i] = dictio.get(i,0) + 1 
        t += str(dictio[i])
    return t

print(numericals('Congratulations'))

# To find nearest square number
def nearest_sq(n):
    return round(n ** 0.5) ** 2

print(nearest_sq(6))

# use of replace
def correct(string):
    return string.replace('1','I').replace('0','O').replace('5','S')

# count no's of 1 in binary bits
def countBits(n):
    return bin(n).count("1")

print(countBits(7))

# longest common sub-sequence
def lcs(x, y):
    if not x or not y: return ""
    if x[0] == y[0]: return x[0] + lcs(x[1:], y[1:])
    
    return max(lcs(x[1:], y), lcs(x, y[1:]), key=len)

print(lcs('cseknowledge','learnknow'))


# use of join
def accum(s):
    return '-'.join([c.upper() + c.lower() * i for i, c in enumerate(s)])

print(accum("$uniL"))

