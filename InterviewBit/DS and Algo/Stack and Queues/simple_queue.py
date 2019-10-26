'''Queue works on the principle of “First-in, first-out”. 
   Time plays an important factor here. 
   We saw that during the implementation of stack we used append() and pop() 
   function which was efficient and fast because we inserted and popped elements from the end of the list, 
   but in queue when insertion and pops are made from the beginning of the list, it is slow. 
   This occurs due to the properties of list, 
   which is fast at the end operations but slow at the beginning operations, 
   as all other elements have to be shifted one by one. So, we prefer the use of collections.
   deque over list, which was specially designed to have fast appends and pops from both the front and back end.
'''


# Python code to demonstrate Implementing  
# Queue using deque and list 
from collections import deque 
queue = deque(["Ram", "Tarun", "Asif", "John"]) 
print(queue) 
queue.append("Akbar") 
print(queue) 
queue.append("Birbal") 
print(queue) 
print(queue.popleft())                  
print(queue.popleft())                  
print(*queue) 



# Python code to demonstrate Implementing  
# queue using list 
queue = ["Amar", "Akbar", "Anthony"] 
queue.append("Ram") 
queue.append("Iqbal") 
print(queue) 
print(queue.pop()) 
print(queue) 
print(queue.pop(0)) 
print(queue) 