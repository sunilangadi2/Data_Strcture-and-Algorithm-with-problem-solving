def solve (arr):
    # Write your code here
    p=arr[0]
    q=arr[1]
    r=arr[2]
    a=arr[3]
    b=arr[4]
    c=arr[5]
    n=arr[6]
    f=[p,q,r]
    if n==0:
        return p
    elif n==1:
        return q
    elif n==2:
        return r
    else:
        for i in range(3,n+1):
            r=a*f[i-1]+b*f[i-2]+c*f[i-3]+g(i)
            f.append(r)
    return f[n]
    
def g(n):
    return n*n*(n+1)

T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))

    out_ = solve(arr)
    print (out_)