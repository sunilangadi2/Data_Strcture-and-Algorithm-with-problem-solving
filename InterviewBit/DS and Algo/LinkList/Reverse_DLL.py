#!/bin/python3

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            
        self.tail = node

def print_doubly_linked_list(node):
    while node:
        print(node.data)
        node = node.next

# Complete the reverse function below.
# Just by reversing the prev and next ponter
# swapping also works but its expensive

def reverse(head):
    tmp=None
    cur=head
    while cur:
        tmp=cur.prev
        cur.prev=cur.next
        cur.next=tmp
        cur=cur.prev
    if tmp:
        head=tmp.prev
    return head

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1)
        #fptr.write('\n')

    #fptr.close()
