import collections

# Function to run a breadth-first-search
# Takes in the board, the size of the board, and the starting location
def bfs(board, size, start):
	queue = collections.deque([[start]])
	seen = set([start])
	visited = [[0 for x in range(size)] for y in range(size)]
	startX, startY = start
	visited[startX][startY] = 1
	
	while queue:
		path = queue.popleft()
		x, y = path[-1]
		
		if board[x][y] == 0:
			return path, visited
		
		for x2, y2 in ((x + board[x][y], y), (x - board[x][y], y), (x, y + board[x][y]), (x, y - board[x][y])):
			
			if 0 <= x2 < size and 0 <= y2 < size and (x2, y2) not in seen:
				queue.append(path + [(x2, y2)])
				seen.add((x2, y2))
				visited[x2][y2] = 1
