def TroubleSort(arr):
    done=False
    while not done:
        for i in range(0,len(arr)-2):
            if arr[i]>arr[i+2]:
                done=False
                arr[i],arr[i+2]=arr[i+2],arr[i]
            else:
                done=True
    
    sort=True 
    e=0

    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            sort=False
            e=i
            break
    
    if sort==True:
        return "OK"
    else:
        return e
            
if __name__ == '__main__':
    print("Enter T")
    T=int(input())

    while(T>0):
        print("Enter n")
        n=input()
        print("Enter array")
        arr=list(map(int,input().split()))
        print(arr)
        print(TroubleSort(arr))
        T-=1

print(TroubleSort([5,6,8,4,3]))
print(TroubleSort([8 ,9 ,7]))
