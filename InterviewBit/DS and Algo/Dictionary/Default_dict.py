# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:15:51 2018

@author: Sunil Angadi
"""

""" demonstrates how to use default dictionary in python"""

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(*i)