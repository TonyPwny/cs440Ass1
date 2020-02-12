import random				#import random for random generation

#function to generate the board and place the start/end points
#returns the built board and its size
def buildBoard():
	#generate a random number between 1 and 4, map 1:5, 2:7, 3:9, 4:11, assign the boardSize variable
	roll = random.randint(1,4)
	if roll == 1:
		boardSize = 5
		
	elif roll == 2:
		boardSize = 7
		
	elif roll == 3:
		boardSize = 9
		
	elif roll == 4:
		boardSize = 11
		
	else:
		return
	#
	
	boardBuilt = [[1 for x in range(boardSize)] for y in range(boardSize)]		#create a 2D array of size "size"x"size" all initialised to 1
	
	i = 0
	j = 0
	
	#code to generate the board, starting with iterating through each row
	while (i < boardSize):
		#iterates through each column of one row, rolling dice and checking if there are too many walls
		while (j < boardSize):
			roll = random.randint(1,(boardSize-1))
			
			#check to see if the number is valid horizontally
			if (i + roll < boardSize) or (i - roll >= 0):
				boardBuilt[i][j] = roll
				
			#check to see if the number is valid vertically
			elif (j + roll < boardSize) or (j - roll >= 0):
				boardBuilt[i][j] = roll
			
			j += 1
		#
		
		j = 0
		i += 1
	#
	
	#make the ending square a 0; always boardBuilt[boardSize-1][boardSize-1]
	boardBuilt[boardSize-1][boardSize-1] = 0
	
	return boardBuilt, boardSize
#
