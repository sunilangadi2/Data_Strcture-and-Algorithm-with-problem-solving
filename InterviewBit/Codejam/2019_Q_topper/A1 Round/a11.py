def solve(t):
    r,c=map(int,input().split())
    mat = [[False for i in range(c)] for i in range(r)] 
    #print(mat)
    result=[]
    p=''
    i=0
    j=0
    pr=0
    pc=0
    mat[i][j]=True
    result.append([i+1,j+1])
    for i in range(0,r):
        for j in range(0,c):
            i=pr
            j=pc
            i+=1
            j+=2
            if i<=r-1 and j<=c-2 :
                while  mat[i][j]==True:
                    j+=1

                mat[i][j]=True
                result.append([i+1,j+1])
            pr=i
            pc=j

    for i in range(0,r):
        for j in range(0,c):
            if mat[i][j]==False:
                p="IMPOSSIBLE"

    if p!="IMPOSSIBLE":
        p="POSSIBLE"
        print('Case #%d: %s' % (t+1,p))
        for l in result:
            print(*l)
    else:
    # output answer
        print('Case #%d: %s' % (t+1,p))

    #print(result)
def main():
    T= int(input())
    for t in range(T):
        solve(t)
        

if __name__ == '__main__':
    main()