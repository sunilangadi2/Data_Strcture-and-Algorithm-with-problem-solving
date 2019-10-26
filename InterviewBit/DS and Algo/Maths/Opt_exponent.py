'''Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative. 
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.

Tc: O(logn) '''


class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        
        res = 1 % d  # Cover case d == 1
        while n > 0:
            if n & 1:   
    # Number becomes odd if num & with 1 returns 1 for even returns 0
               res = (res * x) % d
            x = x**2 %d    # Even
            n >>= 1
        return res

s=Solution()
print(s.pow(2,2,3))
            
               

