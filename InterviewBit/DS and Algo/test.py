class DefaultDict(dict):
    def __missing__(self, key):
        return {key:[]}
d = DefaultDict()
d['1'] = 127
print (d)

def extendList(val, list=[]):
        list.append(val)
        return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
print (list1,list2,list3)


from copy import copy, deepcopy
list1=[34,24,112,25]
list2 = copy(list1)
list3 = deepcopy(list1)
amt = 0
del list2[2:4]
print(list1,list2,list3)
for ls in (list1,list2,list3):
    print(ls)
    if sum(ls)%2==0:
        amt += 20
    if sum(ls)%5==0:
        amt += 5
    if sum(ls)%3==0:
        amt += 10
print (amt)


dic={"r":34,"i":36}
dict1=dic
dict1.update({"i":40,"j":50})
print (dic)


s='sunil angadi'
print("".join(s.split()))

#print(filter(lambda x:x!=" ",s))

L=[3,4,5,6,3]
for i in range(len(L)):
    L[i-1]=L[i]
for i in range(-len(L)):
    print(L[i])