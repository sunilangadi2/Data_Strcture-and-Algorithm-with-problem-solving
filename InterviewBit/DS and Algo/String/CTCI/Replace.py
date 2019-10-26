def ReplaceSpace(String):
    return String.strip().replace(' ','%20')

print(ReplaceSpace("Mr John smith     "))
print(len(locals()))
#print(locals())
print("Here no local variable  is present : ", locals()) 
