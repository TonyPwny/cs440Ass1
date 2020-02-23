# Anthony Tiongson, forked from evaluate class to implement an A* heuristic
# Python2.7
# resources used:
# https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
# https://www.redblobgames.com/pathfinding/a-star/introduction.html
# https://dbader.org/blog/priority-queues-in-python
# https://www.geeksforgeeks.org/stack-in-python/

from queue import PriorityQueue
import copy
import time

# f(n) = estimated total moves to goal where goal is when i = j = size - 1
# f(n) = g(n) + h(n)
# g(n) = moves so far
# h(n) = heuristic estimating how many moves to goal, never overestimate
# 	the heuristic says that for a current position (i, j) and its possible
#		next position (i_2, j_2), if i_2 = size - 1 and if j_2 = size - 1,
# 		the estimated amount of moves left to the goal is only 1.
#	if i_2 = size - 1 or j_2 = size - 1, the estimated amount of moves left
#		to the goal is 2.
#	otherwise, the amount of moves to goal is at least 3.

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
		prevPos[(0, 0)] = None

		while not pQ.empty():

			estimate, i, j, depth = pQ.get()

			self.visited[i][j] = 'Y'
			self.steps[i][j] = depth

			if i == size - 1 and j == size - 1:

				break

			m = board[i][j]

			for i_2, j_2 in ((i-m, j), (i+m, j), (i, j-m), (i, j+m)):

				if (0 <= i_2 < size) and (0 <= j_2 < size) and ((i_2, j_2) not in v):

					if i_2 == size - 1 and j_2 == size - 1:

						estimate = depth + 1
					elif i_2 == size - 1 or j_2 == size - 1:

						estimate = depth + 2
					else:

						estimate = depth + 3

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

		end = time.time()

		self.evalTime = (end - start) * 1000

		# Puzzle Pathfinder for SOLVABLE puzzles
		self.shortestPath = []
		if self.value > 0:

			backtrack = (size - 1, size - 1)

			while backtrack != None:

				self.shortestPath.append(backtrack)
				backtrack = prevPos[backtrack]
