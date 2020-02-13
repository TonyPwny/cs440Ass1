import random				#import random for random generation

# function to generate the board and place the start/end points
# returns the built board and its size
class Board:
	def __init__(self):
		# generate a random number between 1 and 4, map 1:5, 2:7, 3:9, assign the boardSize variable
		# if 4 or any other number not 1,2,3, catch and map as 11
		roll = random.randint(1,4)
		if roll == 1:
			self.boardSize = 5
			
		elif roll == 2:
			self.boardSize = 7
			
		elif roll == 3:
			self.boardSize = 9
			
		else:
			self.boardSize = 11
			
		#
		
		self.boardBuilt = [[1 for x in range(self.boardSize)] for y in range(self.boardSize)]		# create a 2D array of size "size"x"size" all initialised to 1
		
		i = 0
		j = 0
		
		# code to generate the board, starting with iterating through each row
		while (i < self.boardSize):
			# iterates through each column of one row, rolling dice and checking if there are too many walls
			while (j < self.boardSize):
				roll = random.randint(1,(self.boardSize-1))
				
				# check to see if the number is valid horizontally
				if (i + roll < self.boardSize) or (i - roll >= 0):
					self.boardBuilt[i][j] = roll
					
				# check to see if the number is valid vertically
				elif (j + roll < self.boardSize) or (j - roll >= 0):
					self.boardBuilt[i][j] = roll
				
				j += 1
			#
			
			j = 0
			i += 1
		#
		
		# make the ending square a 0; always boardBuilt[boardSize-1][boardSize-1]
		self.boardBuilt[self.boardSize-1][self.boardSize-1] = 0
	#
#
