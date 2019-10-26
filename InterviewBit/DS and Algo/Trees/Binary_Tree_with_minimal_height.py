''' Program to implement Binary Tree with minimal height
    for the given sorted unique array '''

class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'


def initiateArrayToBinary(array):
    return arrayToBinary(array, 0, len(array) - 1)

def arrayToBinary(array, start, end):
    if start > end:
        return ''
    mid = (start + end) // 2
    root = Node(array[mid])
    root.left = arrayToBinary(array, start, mid - 1)
    root.right = arrayToBinary(array, mid + 1, end)
    return root

testArray = [1, 2, 3, 4, 5, 6]
print(initiateArrayToBinary(testArray))