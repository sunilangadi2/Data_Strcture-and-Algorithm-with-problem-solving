
a=[2,4,6,1,2,3,1]
print(a)
# To add element
a.append(5)
print(a)

# To count any element
c=a.count(1)
print(c)

# To add one more list but it remains brackets in the list
b=[7,8,9]
a.append(b)
print(a)

# To add another list as one list
c=[5,6,8]
a.extend(c)
print(a)

# To add string to the list
s='Sunil'
a.append(s)
print(a)

# To get index 
i=a.index(5)
print(i)

# To insert element at specific index syntax: a.insert(index,value)
a.insert(2,10)
print(a)

# To remove last element of array
a.pop()
print(a)

# To remove element at specific index 3
a.pop(3)
print(a)

# To remove element itself specify value
a.remove(10)
print(a)

# To reverse array or list values
a.reverse()
a=a[::-1]
print(a)

