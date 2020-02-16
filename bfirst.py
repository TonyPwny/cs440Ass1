import collections

# Function to run a breadth-first-search
# Takes in the board, the size of the board, and the starting location
class BFS():
	def __init__(self, board, size, start):
		startX, startY = start											# split the start tuple into two variables
		queue = collections.deque([[start]])							# create a deque object at the start location
		seen = set([start])												# create a set for seen tiles
		
		self.visited = [[0 for x in range(size)] for y in range(size)]	# temporary array to document if a tile is visited or not; will be unnecessary with full implementation of steps
		self.visited[startX][startY] = 1								# initialise the start location as visited
		
		self.steps = [[-1 for x in range(size)] for y in range(size)]	# array to hold the number of steps it takes to reach a tile, initialised to '-1'
		self.steps[startX][startY] = 0									# initialise the start location as needing 0 steps
		
		i = 0															# i holds the number of steps as a counter
		# while the queue has elements in it, iterate through possibilities
		while queue:
			path = queue.popleft()										# pops the left element of the queue
			x, y = path[-1]												# splits the most recent element of the queue into x and y
			
			i += 1
			print(i)
			
			#check all possibilities of movement from the tile
			for x2, y2 in ((x + board[x][y], y), (x - board[x][y], y), (x, y + board[x][y]), (x, y - board[x][y])):
				print(x2, y2)
				
				# check to see if the tile is within the bounds
				if (0 <= x2 < size) and (0 <= y2 < size) and ((x2, y2) not in seen):
					queue.append(path + [(x2, y2)])													# add tile to the path
					print(path + [(x2, y2)])
					
					seen.add((x2, y2))																# add the tile to the 'seen' set
					
					self.visited[x2][y2] = 1														# mark the tile as visited
					
					self.steps[x2][y2] = i															# state how many steps it takes to reach the tile
