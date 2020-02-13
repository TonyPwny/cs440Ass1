import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen

def main():
	gameBoard = board.Board()											# builds a Board() object and assigns it to gameBoard
	draw.drawBoard(gameBoard.boardBuilt, gameBoard.boardSize)			# takes the created board and draws it with turtle, as visual output
	
	input("Initial game board displayed.")
	draw.turtle.clear()
#



if __name__ == "__main__":
	main()
#
