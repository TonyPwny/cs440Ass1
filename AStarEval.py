# Anthony Tiongson fork from Fiorilla
# Python2.7

from queue import PriorityQueue
import time
# f(n) = estimated total moves to goal where goal is when i = j = size - 1
# f(n) = g(n) + h(n)
# g(n) = moves so far
# h(n) = heuristic estimating how many moves to goal, never overestimate
# 	the heuristic says that if i = size - 1 or if j = size - 1,
# 		the estimated amount of moves to the goal is 1
#	otherwise, the amount of moves to goal is at least 2 because you need
#		to move at least one more time to fulill the previous scenario

class AStarEval():
	def __init__(self, board, size):
		start = time.time()

		self.visited = [['N' for i in range(size)] for j in range(size)]
		self.steps = [['X' for i in range(size)] for j in range(size)]

		pQ = PriorityQueue()
		v = set()
		prevPos = {}

		pQ.put((2, 0, 0, 0))
		v.add((0, 0))
		prevPos[(0,0)] = None

		while not pQ.empty():
			estimate, i, j, depth = pQ.get()

			print('Current position: (' + str(i) + ', ' + str(j) + ')')
			print('Previous position: ' + str(prevPos[(i, j)]))

			self.visited[i][j] = 'Y'
			self.steps[i][j] = depth

			if i == size - 1 and j == size - 1:
				break

			m = board[i][j]

			for i_2, j_2 in ((i-m, j), (i+m, j), (i, j-m), (i, j+m)):

				if (0 <= i_2 < size) and (0 <= j_2 < size) and ((i_2, j_2) not in v):

					if i_2 == size - 1 or j_2 == size - 1:
						estimate = depth + 1
					else:
						estimate = depth + 2

					pQ.put((estimate, i_2, j_2, self.steps[i][j] + 1))
					v.add((i_2, j_2))
					prevPos[(i_2, j_2)] = (i, j)

		if self.visited[size - 1][size - 1] != 'N':
			self.value = self.steps[size - 1][size - 1]
		else:
			k = 0
			for n in self.visited:
				k -= n.count('N')
			self.value = k

		print('A* evaluation done: solved in ' + str(self.steps[size - 1][size - 1]) + ' moves')
		print('A* value is ' + str(self.value))

		end = time.time()

		self.evalTime = (end - start) * 1000
