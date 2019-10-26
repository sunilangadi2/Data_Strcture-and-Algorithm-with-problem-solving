# Given string of brackets check is it balanced or not

'''
Algorithm:

Whenever an opening bracket appears, we push it onto the stack.
If a closing bracket appears and if it matches the opening bracket 
at the top of the stack, it means that the brackets are balanced and 
we pop the opening bracket out of the stack and continue analyzing 
the string.
If the closing bracket doesn't match the opening bracket at the 
top of the stack, we can infer that the string is not balanced, 
and we print NO.
After processing the string completely and if the stack is empty, 
the string is balanced, and we print YES, else, we print NO.
'''

lefts = '{[('
rights = '}])'
closes = { a:b for a,b in zip(rights,lefts)}

def valid(s):
    stack = []
    for c in s:
        if c in lefts:
            stack.append(c)
        elif c in rights:
            if not stack or stack.pop() != closes[c]:
                return False
    return not stack  # stack must be empty at the end

t = int(input())
for a0 in range(t):    
    s = input()   
    if valid(s):
        print ('YES')
    else:
        print ('NO')