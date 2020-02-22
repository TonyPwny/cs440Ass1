# Thomas Fiorilla
# Module to generate a Board object

import random				#import random for random generation

def valid(i, j, size):
	roll = random.randint(1, max({(size - 1) - i, 0 + i, (size - 1) - j, 0 + j}))

	return roll


# function to generate the board and place the start/end points
# returns the built board and its size
class Board:
	def __init__(self, boardSize):
		# checks to see if the user input board size is valid; if not...
		# generate a random number between 1 and 4, map 1:5, 2:7, 3:9, assign the boardSize variable
		# if 4 or any other number not 1,2,3, catch and map as 11
		# also assigns boardMax, which is the maximum number that will fit in ANY tile

		if int(boardSize) > 4:
			roll = int(boardSize)
		else:
			roll = random.randint(0,3)

		if roll == 0:
			self.boardSize = 5

		elif roll == 1:
			self.boardSize = 7

		elif roll == 2:
			self.boardSize = 9

		elif roll == 3:
			self.boardSize = 11

		else:
			self.boardSize = roll


		self.boardBuilt = [[0 for x in range(self.boardSize)] for y in range(self.boardSize)]		# create a 2D array of size "size"x"size" all initialised to 0

		i = 0
		j = 0

		# code to generate the board, starting with iterating through each row
		while (i < self.boardSize):
			# iterates through each column of one row, rolling dice and checking if there are too many walls
			while (j < self.boardSize):
				if (i == self.boardSize-1) and (j == self.boardSize-1):
					self.boardBuilt[i][j] = 'G'
					break
				else:
					roll = valid(i, j, self.boardSize)

					self.boardBuilt[i][j] = roll

				j += 1

			j = 0
			i += 1
