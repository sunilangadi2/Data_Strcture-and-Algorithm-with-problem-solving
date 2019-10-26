def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        
    return count == 0

print(valid_parentheses('(1*2(3+6)*56))'))