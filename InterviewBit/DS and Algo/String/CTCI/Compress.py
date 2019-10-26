# Compress the string by number of it's char
# Time Complexity: O(n)

def compress(string):
	compressed_string=''
	count=0
	for i in range(0,len(string)):
		count+=1
		if (i+1>=len(string) or string[i]!=string[i+1]):
			compressed_string+= string[i] + str(count)
			count=0
	return compressed_string if len(compressed_string)<len(string) else string

print(compress('aaabcccddeeee'))
