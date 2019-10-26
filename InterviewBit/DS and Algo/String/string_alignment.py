# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:17:42 2018

@author: Sunil Angadi
"""
"""
In Python, a string of text can be aligned left, right and center.

.ljust(width)

This method returns a left aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
.center(width)

This method returns a centered string of length width.

>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
.rjust(width)

This method returns a right aligned string of length width.

>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
"""

import math

c='♥'
width = 40

print ((c*2).center(width//2)*2)

for i in range(1,width//10+1):
    print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
           (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

for i in range(width//4,0,-1):
    print ((c*i*4).center(width))
print ((c*2).center(width))