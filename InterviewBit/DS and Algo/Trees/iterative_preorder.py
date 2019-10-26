# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:28:54 2018

@author: Sunil Angadi
"""

""" The idea is to basically traverse the tree without recursion and by using stack.
 Stack is used here in the same way as used in recursion by 
 first pushing the root and then pushing the right child first
 and then the left child so that left child is processed first
 because stack follows Last-in-first-out(LIFO) property."""
 
class Node:
     def __init__(self,data):
         self.data=data
         self.left=None
         self.right=None

def iterative_preorder(root):
         if root is None:
             return 
         nodestack=[]  # to craete empty stack
         nodestack.append(root)
         
         while(len(nodestack)>0):
             node=nodestack.pop()
             print(node.data,end=' ')
             
             if node.right is not None:
                 nodestack.append(node.right)
                 
             if node.left is not None:
                 nodestack.append(node.left)
             
# Driver program to test above function
if __name__=='__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)
    iterative_preorder(root)        