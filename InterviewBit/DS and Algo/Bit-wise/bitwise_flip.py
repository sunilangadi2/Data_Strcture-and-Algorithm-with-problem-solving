'''
Convert int to binary and flip each bit
of lenth 32 bit and revert it to int
Sample Input 0

3
2147483647
1
0
Sample Output 0

2147483648
4294967294
4294967295'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    return n ^ (2 **32 -1)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        print(result)
