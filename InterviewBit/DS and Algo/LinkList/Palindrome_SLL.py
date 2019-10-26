class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None

    def insert_node(self,data):
        newnode=Node(data)
        tail=self.head

        if self.head==None:
            self.head=newnode
            tail=self.head
        else:
            tail.next=newnode
            tail=newnode

    def is_palindrome(self,ll):
        fast = slow = ll.head
        stack = []

        while fast and fast.next:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()

            if top != slow.data:
                return False

            slow = slow.next

        return True

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        print("Enter n")
        n=int(input())
        slist=SLinkedList()
        for _ in range(n):
            item=int(input())
            slist.insert_node(item)

        print(slist.is_palindrome(slist))
