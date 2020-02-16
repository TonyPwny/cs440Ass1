import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import bfirst

def main():
	gameBoard = board.Board()											# builds a Board() object and assigns it to gameBoard
	
	draw.drawBoard(gameBoard.boardBuilt, gameBoard.boardSize)			# takes the created board and draws it with turtle, as visual output
	path, visited = bfirst.bfs(gameBoard.boardBuilt, gameBoard.boardSize, (0,0))
	print(path)
	input("Initial game board displayed.")
	
	
	draw.drawBoard(visited, gameBoard.boardSize)
	input("Visited tiles displayed.")
#



if __name__ == "__main__":
	main()
#
