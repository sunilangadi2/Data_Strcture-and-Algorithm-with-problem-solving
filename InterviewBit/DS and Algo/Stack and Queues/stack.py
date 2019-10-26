class Stack:
    stack = []  # empty list
    max_size = -1

    def __init__(self, size=-1):  # defining maximum size in the constructor
        self.max_size = size

    def push(self, item):
        if self.max_size == -1:  # if there is no limit in stack
            self.stack.append(item)
        elif len(self.stack) < self.max_size:  # if max limit not crossed
            self.stack.append(item)
        else:  # if max limit crossed
            print('Can\'t add item. Stack limit is :', self.max_size)
            raise RuntimeError

    def pop(self):
        if len(self.stack) > 0:
            temp = self.stack[-1]
            self.stack.pop()
            return temp
        else:
            print('stack is already empty.')
            raise IndexError

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]  # returns the last item
        else:
            print('stack is already empty.')
            raise IndexError

    def display(self):
    	if len(self.stack)==0:
    		print("stack is empty")
    	else:
    		print(*self.stack,end='\n')

st = Stack()
st.push(1)  # push item 1
st.push(2)  # push item 2
st.push(3)
st.push(4)
st.push(5)
print('Pop the last item :', st.pop())  # pop the top item
print('Current top item is :', st.top())  # current top item
st.display()