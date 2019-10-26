#!/usr/bin/env python3

import sys
from collections import Counter


def f(P):
    power = 1
    res = 0
    for c in P:
        if c == 'S':
            res += power
        else:
            power *= 2
    return res

def solve(case_no):
    D = int(input())
    P = input()

    use = 0

    while True:
        if f(P) <= D:
            break
        ids = [i for i in range(len(P) - 1) if P[i:i+2] == 'CS']
        if len(ids) == 0:
            break

        i = ids[-1]
        P = P[:i] + 'SC' + P[i+2:]
        use += 1

    ans = use if f(P) <= D else 'IMPOSSIBLE'

    # output answer
    print('Case #%d: %s' % (case_no, ans))

def main():
    T= int(input())
    for t in range(T):
        solve(t+1)

if __name__ == '__main__':
    main()
