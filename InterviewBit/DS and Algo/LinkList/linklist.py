
# Class Node creates node of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class of singly linked list with specific operation
class SLinkedList:
    def __init__(self):
        self.head = None

    # To print the elements of link list
    def listprint(self):
        start = self.head
        while start is not None:
            print(start.data,end='->')
            start = start.next
        print()  # To start cursor in new line

    # Inserting at the beggining of link list
    def AtBegining(self,newdata):
        # To create Node
        NewNode = Node(newdata)
        # case if head not exist
        if self.head is None:
            self.head = NewNode
            return
        # Update the newnode link to head node if head exist
        NewNode.next = self.head
        self.head = NewNode

    # Inserting at the end of the link list
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next=NewNode

    # Inserting inbetween two nodes
    def Inbetween(self,middle_data,newdata):
        start=self.head
        # To get the link of middle_data
        while start.data!=middle_data:
            start=start.next
        NewNode = Node(newdata) 
        NewNode.next=start.next
        start.next=NewNode

        '''If middle_Node is passed directly
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        # First assign the link to one which is None
        NewNode.next = middle_node.next
        middle_node.next = NewNode'''
        

    # Function to remove node
    def RemoveNode(self, Removekey):
        prev= None
        curr=self.head
        while curr:
            if curr.data==Removekey:
                if prev:
                    prev.next=curr.next
                else:
                    self.head=curr.next
                return
            prev=curr
            curr=curr.next


    def RemoveDuplicates(self):
        if self.head is None:
            return
        runner=self.head
        while runner.next:
            if runner.next.data==runner.data:
                runner.next=runner.next.next
            else:
                runner=runner.next
        return


    def kth_to_last(self, k):
        runner = current = self.head
        for i in range(k):
            if runner is None:
                return None
            runner = runner.next

        while runner:
            current = current.next
            runner = runner.next

        #return current
        while current is not None:
            print(current.data,end='->')
            current=current.next
        print()

    # if direct address of node is given
    def delete_middle_node(self,node):
        node.data = node.next.data
        node.next = node.next.next

    # function to add two list
    def sum_lists(self,ll_a, ll_b):
        n1, n2 = ll_a.head, ll_b.head
        carry = 0
        while n1 or n2:
            result = carry
            if n1:
                result += int(n1.data)
                n1 = n1.next
            if n2:
                result += int(n2.data)
                n2 = n2.next

            v=str(result % 10)
            ll_a.AtEnd(v)
            carry = result // 10

        if carry:
            ll_a.AtEnd(carry)
        print(ll_a)
        #return ll_a
        while ll_a is not None:
            print(ll_a.data,end='->')
            ll_a=ll_a.next
        print()


list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.head.next = e2

# Link second Node to third node
e2.next = e3

# To print all elemnts in link list
list1.listprint()

list1.AtBegining("Sun")

# To print all elemnts in link list
list1.listprint()

list1.Inbetween("Tue","Fri")

list1.listprint()

list1.AtEnd("Thu")

list1.listprint()

list1.RemoveNode("Tue")

list1.listprint()

#ll=SLinkedList()

#ll.generate(100,0,9)

list1.AtBegining("Sun")
print("RemoveDuplicates")
list1.listprint()

list1.RemoveDuplicates()

list1.listprint()

list1.kth_to_last(3)

list1.delete_middle_node(e3)

list1.listprint()

list2 = SLinkedList()
list2.head = Node("1")
list2.head.next=Node("2")
list2.head.next.next=Node("5")

list2.listprint()

list3 = SLinkedList()
list3.head = Node("4")
list3.head.next=Node("6")
list3.head.next.next=Node("8")

list3.listprint()

list3.sum_lists(list2,list3)

list3.listprint()










