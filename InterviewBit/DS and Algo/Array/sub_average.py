def solve(N,a):
    c=0
    result=[]
    for i in range(0,N):
        for j in range(i,N):

            # selected arrray
            lsa=len(a[i:j])+1
            
            if lsa==1:
                sa=sum(a[i:j+1])
            else:
                sa=sum(a[i:j+1])/lsa
            
            # remaining array
            lra=N-lsa-1
            
            if lra==0:
                ra=sum((a[j+1:])+a[:j-1])
            else:
                ra=sum((a[j+1:])+a[:j-1])/lra
        
            if sa>ra:
                c+=1
                result.append([i+1,j+1])
    print(c)
    for n in result:
        print(*n)
                

def main():
    N=int(input())
    a=list(map(int,input().split()))
    r=solve(N,a)
    
if __name__=='__main__':
    main()
    