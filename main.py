import board				#import code for creating the board
import draw					#import code for visually displaying the board on screen

def main():
	gameBoard = board.Board()					# builds a random board and sets the return values equal to boardArray (holds the array) and boardSize (holds the size)
	draw.drawBoard(gameBoard.boardBuilt, gameBoard.boardSize)						# takes the created board and draws it with turtle, as visual output
	
	input("All done!")
#



if __name__ == "__main__":
	main()
#
