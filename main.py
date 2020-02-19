# Thomas Fiorilla
# Main file to execute the code.

import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import evaluate
import hill

def main():
	userInput = input("Enter '5', '7', '9', '11' for a board of that size, or leave blank for a random board. ")
	
	gameBoard = board.Board(userInput)											# builds a Board() object and assigns it to gameBoard
	
	bfs = evaluate.evaluate(gameBoard.boardBuilt, gameBoard.boardSize)		# creates the bfs object
	hillBoard = hill.Hill(gameBoard)
	
	print("Score for the board: " + str(bfs.value))
	
	x = 0
	while x == 0:
		userInput = input("Type '1' for the board, '2' for number of steps, '3' to implement Hill Climbing, '4' to view the Hill Board, anything else to exit. ")
		
		if userInput == '1':
			draw.drawBoard(gameBoard.boardBuilt, gameBoard.boardSize)			# takes the created board and draws it with turtle, as visual output
			print("> Initial game board displayed.")
			print()
		
		elif userInput == '2':
			draw.drawBoard(bfs.steps, gameBoard.boardSize)						# uses the draw module 
			print("> Number of steps to reach a tile displayed.")
			print()
		
		elif userInput == '3':
			userInput = int(input("> How many iterations would you like the hill-climbing to try? "))
			
			while userInput < 0:
				userInput = input("> How many iterations would you like the hill-climbing to try? ")
			
			hillBoard.climb(gameBoard, userInput)
			
			print("> New board score: " + str(hillBoard.score))
		
		elif userInput == '4':
			draw.drawBoard(hillBoard.newPuzzle.boardBuilt, gameBoard.boardSize)			# takes the created board and draws it with turtle, as visual output
			print("> Hill-CLimbing game board displayed.")
			print()
		
		else:
			x = -1
#



if __name__ == "__main__":
	main()
#
