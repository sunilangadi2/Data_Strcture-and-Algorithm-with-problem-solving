
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

def sortedInsert(head, data):
    newnode=DoublyLinkedListNode(data)
    if head==None:
        return newnode
        
    elif data<head.data:
        newnode.next=head
        head.prev=newnode
        return newnode
    else:
        rest=sortedInsert(head.next,data)
        head.next=rest
        rest.prev=head
        return head

if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1)
    
