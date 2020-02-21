# Anthony Tiongson fork from Fiorilla
# Python2.7

from queue import PriorityQueue
import time
# f(n) = total moves to goal where goal is when i = j = size - 1
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
		prevPos = {}
		moves = {}

		pQ.put((0, 0), 0)
		prevPos[(0, 0)] = None
		moves[(0, 0)] = 0

		while not pQ.empty():
			i, j = pQ.get()
			print('Current position: (' + str(i) + ', ' + str(j) + ')')
			print('Previous position: ' + str(prevPos[(i, j)]))

			self.visited[i][j] = 'Y'
			self.steps[i][j] = moves[(i, j)]

			if i == size - 1 and j == size - 1:
				break

			m = board[i][j]

			# for ALL possible positions i_2, j_2 from the current position,
			# 	including invalid ones
			for i_2, j_2 in ((i-m, j), (i+m, j), (i, j-m), (i, j+m)):

				# if the next subsequent coordinate i_2, j_2 is valid with respect
				#	to the size of the puzzle board
				if (0 <= i_2 < size) and (0 <= j_2 < size) and (i_2, j_2) not in moves:

					moves[(i_2, j_2)] = moves[(i, j)] + 1
					m_2 = board[i_2][j_2]

					if (i_2 == size - 1 and i_2 == size - 1):
						heuristic = 0
					elif (i_2 == size - 1 or j_2 == size - 1):
						heuristic = 1
					else:
						heuristic = 2

					for i_3, j_3 in ((i_2-m_2, j_2), (i_2+m_2, j_2), (i_2, j_2-m_2), (i_2, j_2+m_2)):

						if (0 <= i_2 < size) and (0 <= j_2 < size) and (i_2, j_2):

							if (i_3 == size - 1 and i_3 == size - 1):
								heuristic_2 = 0
							elif (i_3 == size - 1 or j_3 == size - 1):
								heuristic_2 = 1
							else:
								heuristic_2 = 2

							priority = moves[(i_2, j_2)] + heuristic + heuristic_2
							pQ.put((i_2, j_2), priority)
							prevPos[(i_2, j_2)] = (i, j)


		if self.visited[size - 1][size - 1] != 'N':
			self.value = self.steps[size - 1][size - 1]
		else:
			k = 0
			for n in self.visited:
				k -= n.count('N')
			self.value = k

		print('A* evaluation done: solved in ' + str(moves[(size - 1, size - 1)]))

		end = time.time()

		self.evalTime = (end - start) * 1000
