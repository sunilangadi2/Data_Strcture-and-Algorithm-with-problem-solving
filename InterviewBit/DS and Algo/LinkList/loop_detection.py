# Given a circular linked list return the node at which 
# loop occurs

''' Design:
    Initially keep two fast and slow pointer
    if there is a loop then they collide each other
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None

    def insert_node(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            return self.head
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=newnode
            return self.head

    def loop_point(self,head):
        slow=self.head
        fast=self.head

        # find meeting point of length LOOP_SIZE - k
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            # Collision
            if fast==slow:
                break

        # No collision,No loop
        if fast==None or fast.next==None:
            return None

        '''Move slow to head,keep fast at the meeting point.
        Each are k steps from the loop start,If they move at the same pace
        they must meet at the loop start'''
        slow=self.head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return fast

    def print_linked_list(self,head):
        node=self.head
        while node:
            print(node.data)
            node = node.next

if __name__ == '__main__':
    list1=SLinkedList()
    n=int(input()) 
    for _ in range(n):
        d=int(input())
        list1.insert_node(d)

    print(list1.loop_point(list1))
    list1.print_linked_list(list1)




