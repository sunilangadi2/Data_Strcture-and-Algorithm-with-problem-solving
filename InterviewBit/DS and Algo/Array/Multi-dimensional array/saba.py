def match(r,c,word):
	match = 0
	if(grid[r][c] != word[0]):
		return False
 
	for d in range(0,4):
		rd = r + x[d]
		cd = c + y[d]
		result = 0
		for k in range(1,4):
			if(rd<0 or rd>=n or cd<0 or cd>=m):
				break
			if(grid[rd][cd] != word[k]):
				break
			result = result + 1
			rd = rd + x[d]
			cd = cd + y[d]
		if result == 3:
			match = match + 1
	return match
 
n,m = list(map(int,input().split()))
grid = [None]*n

a = 0
length = 4
x = [-1,0,1,1]
y = [1,1,1,0]
for _ in range(n):
	s = input().strip()
	grid[a] = s
	a = a + 1
res = 0
for i in range(n):
	for j in range(m):
		res = res + match(i,j,'saba')
 
print(res)