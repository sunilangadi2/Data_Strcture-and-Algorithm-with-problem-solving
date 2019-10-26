''' Program to print depth first search traversal of graph'''

from collections import defaultdict

class graph:

	def __init__(self):
		self.graph=defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)
		

	# Function to print DFS of a graph
	# each recursive call internally uses satck	
	def dfs(self,graph, node, visited):
	    if node not in visited:
	        visited.append(node)
	        for n in self.graph[node]:
	            self.dfs(self.graph,n, visited)
	    return visited


# Driver code 
  
# Create a graph given in 
# the above diagram 
g = graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Depth First Traversal"
                  " (starting from vertex 2)") 

traversal = g.dfs(graph,1, [])
for node in traversal:
	print(node,end='->')


