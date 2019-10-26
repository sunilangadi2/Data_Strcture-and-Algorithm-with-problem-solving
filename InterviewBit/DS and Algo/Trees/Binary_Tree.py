''' Program to implement Binary Tree '''

class TreeNode:
    # Creating structure of TreeNode
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Tree:
    def __init__(self):
        self.root = None
        self.height=0
    # creating the tree based on Binary Search Tree principle
    def addNode(self, node, value):
        if(node==None):
            self.root = TreeNode(value)
        else:
            if(value<node.data):
                if(node.left==None):
                    node.left = TreeNode(value)
                else:
                    self.addNode(node.left, value)
            else:
                if(node.right==None):
                    node.right = TreeNode(value)
                else:
                    self.addNode(node.right, value)

    def printInorder(self, node):
        if node!=None:
            self.printInorder(node.left)
            print(node.data)
            self.printInorder(node.right)

    def printPreorder(self,node):
        if node!=None:
            print(node.data)
            self.printPreorder(node.left)
            self.printPreorder(node.right)

    def printPostorder(self,node):
        if node!=None:
            self.printPostorder(node.left)
            self.printPostorder(node.right)
            print(node.data)

    def printLevelOrder(self,root): 
        # Base Case 
        if root is None: 
            return
          
        # Create an empty queue for level order traversal 
        queue = [] 
      
        # Enqueue Root and initialize height 
        queue.append(root) 
      
        while(len(queue) > 0): 
            # Print front of queue and remove it from queue 
            print(queue[0].data) 
            node = queue.pop(0) 
      
            #Enqueue left child 
            if node.left is not None: 
                queue.append(node.left) 
      
            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right)

                 
    # printing level order traversal of given level
    def printLevelOrder_gevenLevel(self,root,level): 
        # Base Case 
        if root is None: 
            return
          
        # Create an empty queue for level order traversal 
        queue = [] 
      
        # Enqueue Root and initialize height 
        queue.append(root) 

        if level==0:
            print(queue[0].data)
            return
        c=0
        n=level*2
        while(len(queue) > 0): 
            # Print front of queue and remove it from queue 
            c+=1
            #print(queue[0].data) 
            node = queue.pop(0) 
      
            #Enqueue left child 
            if node.left is not None: 
                queue.append(node.left)
            
            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right) 
            

            if c==level:
                k=1
                while k!=n:
                    print(queue.pop().data)
                    k+=1
                return
    
def main():
    testTree = Tree()
    testTree.addNode(testTree.root, 200)
    testTree.addNode(testTree.root, 300)
    testTree.addNode(testTree.root, 100)
    testTree.addNode(testTree.root, 30)
    testTree.addNode(testTree.root,10)
    print("Inorder Traversal")
    testTree.printInorder(testTree.root)
    print("Preorder Traversal")
    testTree.printPreorder(testTree.root)
    print("Postorder Traversal")
    testTree.printPostorder(testTree.root)
    print("Level order Traversal")
    testTree.printLevelOrder(testTree.root)
    print("Level order Traversal at given level")
    testTree.printLevelOrder_gevenLevel(testTree.root,2)
      
if __name__ == '__main__':
    main()
