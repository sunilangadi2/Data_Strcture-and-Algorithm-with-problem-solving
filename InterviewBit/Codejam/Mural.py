def solve():
    n=int(input())
    # It just reads the array values without space
    arr=list(x for x in input())
    print(arr)
    c=n//2

    return 10


def main():
    T= int(input())
    for t in range(T):
        a=solve()
        # output answer
        print('Case #%d: %d' % (t+1, a))

if __name__ == '__main__':
    main()