from collections import defaultdict

class Node:
	def __init__(self, data):
		self.vertex = data
		self.next = None
	#
#

# This class represents a directed graph using adjacency list representation
class BreadthFirst:
	# constructor
	def __init__(self, boardBuilt, boardSize):
		# default dictionary to store graph 
		#self.graph = defaultdict(list) 
		self.graph = [[Node(None) for x in range(boardSize)] for y in range(boardSize)]
		self.board = boardBuilt
		self.stepsTaken = [[-1 for x in range(boardSize)] for y in range(boardSize)]
	
	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v)
	
	# Function to print a BFS of graph 
	def bfs(self, s):
		# Mark all the vertices as not visited 
		visited = [False] * (len(self.graph)) 
		
		# Create a queue for BFS 
		queue = [] 
		
		# Mark the source node as visited and enqueue it 
		queue.append(s) 
		visited[s] = True
		
		while queue: 
			# Dequeue a vertex from queue and print it 
			s = queue.pop(0) 
			print (s, end = " ") 
			
			# Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it visited and enqueue it 
			for i in self.graph[s]: 
				if visited[i] == False: 
					queue.append(i) 
					visited[i] = True
