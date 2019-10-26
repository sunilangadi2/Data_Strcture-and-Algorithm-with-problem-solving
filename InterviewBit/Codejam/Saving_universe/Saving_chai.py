from collections import Counter
def solve(d,st):
    n=len(st)
    cos,coc=0,0
    for i in range(0,n):
        if st[i]=='s':
            cos+=1
        else:
            coc+=1

    if n==0 or n==1 or coc==0 or cos==0:
        return 0

    c=1
    for i in range(0,cos+1):
        if st[i]==st[i+1]:
            c+=1
        else:
            break
    print(c,cos)
    if c==cos:
        return 0
    
    return 1

def main():
    T = int(input())
    for t in range(T):
        d=int(input())
        st=input()
        ans=int(solve(d,st))
        print('Case #%d: %d' % (t, ans))

if __name__ == '__main__':
    main()