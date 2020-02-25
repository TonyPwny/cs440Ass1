# Thomas Fiorilla
# Fork of Anthony Tiongson evaluate class to simply return the final result; code is 99% Anthony's

from queue import Queue

def evaluate(board, size):
	visited = [['N' for i in range(size)] for j in range(size)]
	steps = [['X' for i in range(size)] for j in range(size)]
	
	q = Queue()
	v = set()
	depth = 0
	
	q.put((0, 0, depth))
	v.add((0, 0))
	
	while not q.empty():
		i, j, d = q.get()
		
		m = board[i][j]
		visited[i][j] = 'Y'
		steps[i][j] = d
		
		for i_2, j_2 in ((i-m, j), (i+m, j), (i, j-m), (i, j+m)):
			if (0 <= i_2 < size) and (0 <= j_2 < size) and ((i_2, j_2) not in v):
				q.put((i_2, j_2, steps[i][j] + 1))
				v.add((i_2, j_2))
				
	if visited[size - 1][size - 1] != 'N':
		value = steps[size - 1][size - 1]
	else:
		k = 0
		for n in visited:
			k -= n.count('N')
		value = k
		
	return value
