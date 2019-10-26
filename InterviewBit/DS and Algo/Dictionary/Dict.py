
def solve(s1,s2):
    dic={}
    count=0
    for char in s2:
        if char in dic:
            dic[char]+=1
        else:
            dic[char]=1

    for c in s1:
        if c in dic:
            count+=1
            dic[c]-=1

    print(count)
        

if __name__ == '__main__':
    t=int(input())
    while t:
        n=int(input())
        t1=input()
        t2=input()
        solve(t1,t2)
        t-=1