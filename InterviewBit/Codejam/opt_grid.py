def solve():
	# reading grid dimension
	N=int(input())
	n=((N-1)*2)//2
	s=input()

	rs=''

	for c in s:
		if c=='S':
			rs+='E'
		else:
			rs+='S'
	return rs


def main():
    T= int(input())
    for t in range(T):
        rs=solve()
        # output answer
        print('Case #%d: %s' % (t+1,rs))

if __name__ == '__main__':
    main()