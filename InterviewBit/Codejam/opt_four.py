def solve():
    N=input()
    
    f=int(N)

    if f==4:
        return 2,2

    cn=str(f)

    n=len(cn)

    l=[]
    a=''
    b=''
    for i in range(0,n):
        if cn[i]=='4':
            a+='3'
            l.append(i)
        else:
            a+=cn[i]

    z=[0]* len(a)
    

    for d in l:
        z[d]=1

   

    for d in z:
        b+=str(d)
    
    b=int(b)
    a=int(a)
    return a,b


def main():
    T= int(input())
    for t in range(T):
        a,b=solve()
        # output answer
        print('Case #%d: %d %d' % (t+1, a,b))

if __name__ == '__main__':
    main()