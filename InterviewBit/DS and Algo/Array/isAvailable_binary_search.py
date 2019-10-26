# -*- coding: utf-8 -*-
"""
Created on Sat May  5 10:16:36 2018

@author: Sunil Angadi
"""
""" It returns true if the user entered name is not in the users list 
    otherwise returns false"""
    
""" By using binary search recursively chacking the middle element with
    username  """
    
# search method is binary search hence users list should be in sorted sequence
users = ['amy', 'bob', 'charlie','sunil']

def is_available(username, users):
    if len(users) == 0:
        return True
    elif len(users) == 1:
        return username != users[0]
    else:
        mid = int(len(users)/2)
        if username == users[mid]:
            return False
        elif username < users[mid]:
            return is_available(username, users[:mid])
        else:
            return is_available(username, users[mid:])
        

print(is_available('sunil', users))