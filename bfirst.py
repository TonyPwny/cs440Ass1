import collections

def bfs(board, size, start):
	queue = collections.deque([[start]])
	seen = set([start])
	
	while queue:
		path = queue.popleft()
		x, y = path[-1]
		
		if board[x][y] == 0:
			return path
		
		#for x2, y2 in ((x + board[x][y], y), (x - board[x][y], y), (x, y + board[x][y]), (x, y - board[x][y])):
		for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
			if 0 <= x2 < size and 0 <= y2 < size and (x2, y2) not in seen:
				queue.append(path + [(x2, y2)])
				seen.add((x2, y2))
