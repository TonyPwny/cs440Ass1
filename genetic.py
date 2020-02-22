# Anthony Tiongson, forked from Thomas Fiorilla's hill class
# Python2.7

import copy
import AStarEval
import bfirst
import random
import board
import time

class genetic:
	def __init__(self, board):
		self.puzzle = copy.deepcopy(board)

	def mutate(self, iterations):
		start = time.time()

		n_max = self.puzzle.boardSize - 1
		newPuzzle = copy.deepcopy(self.puzzle)
		count = 1

		while iterations > 0:
			# print('Iteration: ' + str(count))
			eval1 = bfirst.evaluate(self.puzzle.boardBuilt, self.puzzle.boardSize)
			i_r = random.randint(0, n_max)

			if i_r == n_max:
				j_r = random.randint(0, (n_max - 1))
			else:
				j_r = random.randint(0, n_max)

			newPuzzle.boardBuilt[i_r][j_r] = board.valid(i_r, j_r, self.puzzle.boardSize)

			eval2 = bfirst.evaluate(newPuzzle.boardBuilt, self.puzzle.boardSize)

			if eval2 > eval1:
				# print('Hill Climbing mutation better')
				self.puzzle = copy.deepcopy(newPuzzle)
				eval = bfirst.evaluate(self.puzzle.boardBuilt, self.puzzle.boardSize)
			else:
				# print('Original puzzle better or as good')
				eval = bfirst.evaluate(self.puzzle.boardBuilt, self.puzzle.boardSize)

			count += 1
			iterations -= 1

		self.score = bfirst.evaluate(self.puzzle.boardBuilt, self.puzzle.boardSize)

		end = time.time()

		self.evalTime = (end - start) * 1000
