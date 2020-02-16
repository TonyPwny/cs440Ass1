import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import bfirst

def main():
	gameBoard = board.Board()											# builds a Board() object and assigns it to gameBoard
	
	bfs = bfirst.BFS(gameBoard.boardBuilt, gameBoard.boardSize, (0,0))		# creates the bfs object
	#print(bfs.path)															# prints a path to the console if available
	
	x = 0
	while x == 0:
		userInput = input("Type '1' for the board, '2' for the visited matrix, '3' for number of steps, anything else to exit. ")
		
		if userInput == '1':
			draw.drawBoard(gameBoard.boardBuilt, gameBoard.boardSize)			# takes the created board and draws it with turtle, as visual output
			print("> Initial game board displayed.")
			print()
		
		elif userInput == '2':
			draw.drawBoard(bfs.visited, gameBoard.boardSize)
			print("> Visited tiles displayed.")
			print()
		
		elif userInput =='3':
			draw.drawBoard(bfs.steps, gameBoard.boardSize)
			print("> Number of steps to reach a tile displayed.")
			print()
		
		else:
			x = -1
#



if __name__ == "__main__":
	main()
#
