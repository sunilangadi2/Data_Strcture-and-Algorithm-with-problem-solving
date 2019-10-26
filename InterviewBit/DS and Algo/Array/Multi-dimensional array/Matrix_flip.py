m,n,k=map(int,input().split())
n=n-1
m=m-1
mat = [[j for j in input().split()] for i in range(n)]

ncz=[]
for i in range(0,m):
	nz=0
	for j in range(0,n):
		if mat[i][j]=='0':
			nz+=1
	ncz.append(nz)


c=[]
for i in range(0,len(ncz)):
	if ncz[i]<=k:
		c.append(i)


res=1
for r1,r2 in zip(c[:],c[1:]):
	f=True
	for j in range(0,n):
		if mat[r1][j]!=mat[r2][j]:
			f=False
	if f==True:
		res+=1
print(res)

