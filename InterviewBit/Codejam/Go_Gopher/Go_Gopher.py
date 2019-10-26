#!/usr/bin/env python3

import sys
import math
from itertools import product

def flush():
    sys.stdout.flush()

def read_str():
    return input()

def read_strs():
    return list(input().split())

def read_ints():
    return list(map(int, input().split()))

def solve(case_no):
    A, = read_ints()
    DIM = 1000  # Note the off-by-1 of ours (0-999) and judges (1-1000)

    # we only care an X-by-Y region
    X = int(math.sqrt(A))
    Y = A // X
    while X * Y < A:
        Y += 1

    # print(A, X, Y, file=sys.stderr)

    c = [[1 for j in range(Y)] for i in range(X)]  # 1 for not digged

    def get_sum(x, y):
        return (
            c[x-1][y-1] + c[x-1][y] + c[x-1][y+1] +
            c[x][y-1] + c[x][y] + c[x][y+1] +
            c[x+1][y-1] + c[x+1][y] + c[x+1][y+1]
        )

    while True:
        bs, bx, by = 0, 0, 0
        for x, y in product(range(1, X-1), range(1, Y-1)):
            # x, y is the center of 3-by-3 region
            s = get_sum(x, y)

            if s > bs:
                bs, bx, by = s, x, y

            if s == 9:
                break

        print(bx + 1, by + 1)
        flush()
        x, y = read_ints()
        if x == 0 and y == 0:
            break
        if x == -1 and y == -1:
            exit(1)
        x -= 1
        y -= 1
        c[x][y] = 0

        # print(c, file=sys.stderr)


def main():
    T, = read_ints()
    for t in range(T):
        solve(t+1)

if __name__ == '__main__':
    main()
