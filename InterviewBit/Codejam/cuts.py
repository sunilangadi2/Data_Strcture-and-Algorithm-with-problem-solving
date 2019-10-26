def solve():
    # reading r,c,h,v
    r,c,h,v=map(int,input().split())
    csr=[0]*r
    csc=[0]*c
    print(csr,csc)
    M = [[0]*c]*r 
    print(M)

    m=[]
    for i in range(r):
        a=list(input().split())
    m.append(a)
    print(m)

    print(csr,csc)


def main():
    T= int(input())
    for t in range(T):
        rs=solve()
        # output answer
        print('Case #%d: %s' % (t+1,rs))

if __name__ == '__main__':
    main()