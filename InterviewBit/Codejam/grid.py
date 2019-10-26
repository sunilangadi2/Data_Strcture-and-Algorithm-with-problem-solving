def solve():
	# reading grid dimension
	N=int(input())
	n=((N-1)*2)//2
	s=input()

	if N==2:
		return s[::-1]
	
	xe=0
	xs=0

	rs=''
	i=0
	c=0
	while c<n:

		if s[i:i+2]=='EE':
			rs+='ES'
			xs+=1
			

		elif s[i:i+2]=='SS':
			rs+='ES'
			xe+=1
			

		elif s[i:i+2]=='SE':
			rs+='ES'
			xe+=1
			
		elif s[i:i+2]=='ES':
			rs+='SE'
			xs+=1
			

		i=i+2
		c=c+1

	l=list(rs)
	
	while xs > xe:
		for c in l:
			if c =='E':
				idx=l.index(c)
				l[idx]='S'
				xe+=1
				break
	
	while xe > xs:
		for c in l:
			if c =='S':
				idx=l.index(c)
				l[idx]='E'
				xs+=1
				break

	rs=''.join(l)
	return rs


def main():
    T= int(input())
    for t in range(T):
        rs=solve()
        # output answer
        print('Case #%d: %s' % (t+1,rs))

if __name__ == '__main__':
    main()