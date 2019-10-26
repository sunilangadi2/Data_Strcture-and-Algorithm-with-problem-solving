#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the checkMagazine function below.

def checkMagazine(mag, note):
    d=dict(Counter(mag))
    f=0
    for w in note:
        if w in d:
            d[w]=d[w]-1
            if d[w]==0:
                del d[w]
        else:
            f=1
    if f==0:
        print('Yes')
    else:
        print('No')


def ransom_note(magazine, rasom):
    print(Counter(magazine))
    return (Counter(rasom) - Counter(magazine)) == {}


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
    print(ransom_note(magazine, note))

