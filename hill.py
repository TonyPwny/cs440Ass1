# Thomas Fiorilla, fork of Anthony Tiongson
# Fork of Anthony's code so that the hill-climbing is its own module; 95% of code is Anthony's, remaining 5% is adapting code to be a class

import copy
import bfirst
import random

class Hill:
	def __init__(self, board):
		self.newPuzzle = copy.deepcopy(board)
	
	def climb(self, puzzle, iterations):
		n_max = puzzle.boardSize - 1
		
		count = 1
		
		while iterations > 0:
			print('Iteration: ' + str(count))
			eval1 = bfirst.evaluate(puzzle.boardBuilt, puzzle.boardSize)
			
			self.newPuzzle.boardBuilt[0][0] = 1
			
			i_r = random.randint(0, n_max)
			
			if i_r == n_max:
				j_r = random.randint(0, (n_max - 1))
			else:
				j_r = random.randint(0, n_max)
				
			valid = False
			while valid is not True:
				rand = random.randint(1, n_max)
				if (i_r + rand < n_max) or (i_r - rand >= 0):
					self.newPuzzle.boardBuilt[i_r][j_r] = rand
					print('Successful Random Found')
					valid = True
				elif (j_r + rand < n_max) or (j_r - rand >= 0):
					self.newPuzzle.boardBuilt[i_r][j_r] = rand
					print('Successful Random Found')
					valid = True
				else:
					print('Unsuccessful Random')
				
			eval2 = bfirst.evaluate(self.newPuzzle.boardBuilt, puzzle.boardSize)
				
			if eval2 > eval1:
				print('Hill Climbing mutation better')
				puzzle = copy.deepcopy(self.newPuzzle)
				eval = bfirst.evaluate(puzzle.boardBuilt, puzzle.boardSize)
				self.score = eval2
			else:
				print('Original puzzle better or as good')
				eval = bfirst.evaluate(puzzle.boardBuilt, puzzle.boardSize)
				self.score = eval1
				
			count += 1
			iterations -= 1
