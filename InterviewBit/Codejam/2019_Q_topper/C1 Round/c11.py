def solve():
    A=int(input())
    c=[]
    for i in range(0,A):
        s=input()
        c.append(s)
    cr,cs,cp=0,0,0

    if A==1:
        for g in c:
            if g=='RS':
                return 'RSRSRSP'
            elif g=='RP':
                return 'RPRPRPS'
            elif g=='SP':
                return 'SPSPSPR'
            elif g=='SR':
                return 'SRSRSRP'
            elif g=='PR':
                return 'PRPRPRS'
            elif g=='PS':
                return 'PSPSPSR'

    for g in c:
        if g=='R':
            cr+=1
        elif g=='S':
            cs+=1
        elif g=='P':
            cp+=1
    if cr==1 and cs==1 and cp==1:
        return 'IMPOSSIBLE'
    rsf=0
    rpf=0
    spf=0
    for g in c:
        if g!='RS':
            rsf=1
        if g!='RP':
            rpf=1
        if g!='SP':
            spf=1
    if rsf==0:
        return 'P'
    if rpf==0:
        return 'S'
    if spf==0:
        return 'R' 


def main():
    T= int(input())
    for t in range(T):
        r=solve()
        # output answer
        print('Case #%d: %s' % (t+1,r))

if __name__ == '__main__':
    main()