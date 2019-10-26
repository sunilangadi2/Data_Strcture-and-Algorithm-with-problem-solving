from collections import Counter

c  = "a turtle on a fence had help"

print(dict(Counter(c.split())))



sentence = 'a turtle on a fence had help'
output = {}
for word in sentence.split():
    if word not in output.keys():
        output[word] = 0
    output[word] += 1

print(output)


# function to return key for any value 
def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"
  
# Driver Code 
  
my_dict ={"java":100, "python":112, "c":11} 
  
print(get_key(100)) 
print(get_key(11)) 