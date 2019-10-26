# -*- coding: cp1252 -*-
'''Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120 
Number of trailing zeros = 1
So, return 1
Seen this question in a real interview beforeYesNo'''

'''The idea is:

The ZERO comes from 10.

The 10 comes from 2 x 5

And we need to account for all the products of 5 and 2, like 4×5 = 20 …

So, if we take all the numbers with 5 as a factor, we will have plenty of even numbers to pair with them to get factors of 10

Example 1:

How many multiples of 5 are there between 1 and 23?

These are 5, 10, 15, and 20, for four multiples of 5. Paired with 2s from the even factors, this makes for four factors of 10, so: 23! has 4 zeros.

'''


def trailingZeroes(x):
        i = 5
        zeros = 0
        while x >= i:
            zeros += x // i
            i *= 5
        return zeros
print(trailingZeroes(23))

