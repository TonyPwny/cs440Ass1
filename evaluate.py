# Anthony Tiongson, forked from Thomas Fiorilla's bfirst attempt
# Python2.7
# resources used:
# https://www.youtube.com/watch?v=pcKY4hjDrxk&t=377s

from queue import Queue
import time

class evaluate():

	def __init__(self, board, size):

		start = time.time()

		self.visited = [['N' for i in range(size)] for j in range(size)]
		self.steps = [['X' for i in range(size)] for j in range(size)]

		q = Queue()
		v = set()
		prevPos = {}

		q.put((0, 0, 0))
		v.add((0, 0))
		prevPos[(0, 0)] = None

		while not q.empty():

			i, j, depth = q.get()

			self.visited[i][j] = 'Y'
			self.steps[i][j] = depth
			if i == size - 1 and j == size - 1:

				m = 0
			else:

				m = board[i][j]

			for i_2, j_2 in ((i-m, j), (i+m, j), (i, j-m), (i, j+m)):

				if (0 <= i_2 < size) and (0 <= j_2 < size) and ((i_2, j_2) not in v):

					q.put((i_2, j_2, self.steps[i][j] + 1))
					v.add((i_2, j_2))
					prevPos[(i_2, j_2)] = (i, j)

		if self.visited[size - 1][size - 1] != 'N':

			self.value = self.steps[size - 1][size - 1]
		else:

			k = 0

			for n in self.visited:

				k -= n.count('N')

			self.value = k

		end = time.time()

		self.evalTime = (end - start) * 1000

		# Puzzle Pathfinder for SOLVABLE puzzles
		self.shortestPath = []
		if self.value > 0:

			backtrack = (size - 1, size - 1)

			while backtrack != None:

				self.shortestPath.append(backtrack)
				backtrack = prevPos[backtrack]
