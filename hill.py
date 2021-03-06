# Thomas Fiorilla, fork of Anthony Tiongson
# Fork of Anthony's code so that the hill-climbing is its own module and class; 95% of code is Anthony's, remaining 5% is adapting code to be a class

import copy
import bfirst
import evaluate
import random
import board
import time

class Hill:
	def __init__(self, board):
		self.puzzle = copy.deepcopy(board)
		self.averageScore = []
		
	def climb(self, iterations):
		start = time.time()
		
		n_max = self.puzzle.boardSize - 1
		newPuzzle = copy.deepcopy(self.puzzle)
		count = 1
		
		while iterations > 0:
			# print('Iteration: ' + str(count))
			eval1 = evaluate.evaluate(self.puzzle.boardBuilt, self.puzzle.boardSize).value
			i_r = random.randint(0, n_max)
			
			if i_r == n_max:
				j_r = random.randint(0, (n_max - 1))
			else:
				j_r = random.randint(0, n_max)
				
			newPuzzle.boardBuilt[i_r][j_r] = board.valid(i_r, j_r, self.puzzle.boardSize)
			
			eval2 = evaluate.evaluate(newPuzzle.boardBuilt, self.puzzle.boardSize).value
			
			if eval2 >= eval1:
				# print('Hill Climbing mutation better')
				self.puzzle = copy.deepcopy(newPuzzle)
				eval = evaluate.evaluate(self.puzzle.boardBuilt, self.puzzle.boardSize).value
			else:
				# print('Original puzzle better or as good')
				eval = evaluate.evaluate(self.puzzle.boardBuilt, self.puzzle.boardSize).value
				
			count += 1
			iterations -= 1
			
		self.score = evaluate.evaluate(self.puzzle.boardBuilt, self.puzzle.boardSize).value
		
		end = time.time()
		
		self.evalTime = (end - start) * 1000
