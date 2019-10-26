def solve(N, A):
    # print "Input:", N, A
    B = [0] * (N + 1)
    print(B)
    for i in range(1, N + 1):
        B[i] = B[i - 1] + A[i - 1]
    print(B)
    res = 0
    half = (N + 1) // 2
    for i in range(N):
        if i + half <= N:
            res = max(res, B[i + half] - B[i])
    return res


def main():

    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().strip()))
        res = solve(N, A)
        out = "Case #%d: %s\n" % (i + 1, res)
        # print out
        print(out)
        # fo.write(out)


main()
