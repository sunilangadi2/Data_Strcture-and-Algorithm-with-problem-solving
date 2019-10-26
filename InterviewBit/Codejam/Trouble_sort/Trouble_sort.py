#!/usr/bin/env python3

import sys
from collections import Counter
'''
def read_str():
    return input()

def read_strs():
    return list(input().split())

def read_ints():
    return list(map(int, input().split()))
'''
def solve(case_no):
    N = int(input())
    V = list(map(int,input().split()))

    # even, odd
    # indx start from 0
    V_even = [_ for i, _ in enumerate(V) if i % 2 == 0]
    V_odd = [_ for i, _ in enumerate(V) if i % 2 == 1]

    V_even.sort()
    V_odd.sort()

    # reconstruct
    V_res = []
    n_even, n_odd = len(V_even), len(V_odd)
    for i in range(max(n_even, n_odd)):
        if i < n_even:
            V_res.append(V_even[i])
        if i < n_odd:
            V_res.append(V_odd[i])

    ans = 'OK'
    for i in range(N - 1):
        if V_res[i] > V_res[i+1]:
            ans = i
            break
    # output answer
    print('Case #%d: %s' % (case_no, ans))

def main():
    T = int(input())
    for t in range(T):
        solve(t+1)

if __name__ == '__main__':
    main()
