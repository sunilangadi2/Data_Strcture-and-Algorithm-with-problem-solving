def solve():
    N=input()
    n=len(N)
    f=int(N)
    r=f

    if f==4:
        return 2,2

    x=0
    while r>0:
        N=r
        lt=str(N)
        lt=lt[n-2:]
        x=f-r

        if int(lt)%4==0:
            a=N//4
            b=N-a
            a=a+x

            if '4' not in str(a) and '4' not in str(b) and a+b==f:
                return a,b

            a=a-x
            b=b+x

            if '4' not in str(a) and '4' not in str(b) and a+b==f:
                return a,b

            r=N-3

        else:
            r=N-3


def main():
    T= int(input())
    for t in range(T):
        a,b=solve()
        # output answer
        print('Case #%d: %d %d' % (t+1, a,b))

if __name__ == '__main__':
    main()