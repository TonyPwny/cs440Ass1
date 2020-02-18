# Anthony Tiongson fork from Fiorilla
# Python2.7

import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import BFSearch
import HillClimb

def mainAT():
	gameBoard = board.Board()											# builds a Board() object and assigns it to gameBoard

	bfs = BFSearch.BFSearch(gameBoard.boardBuilt, gameBoard.boardSize)		# creates the bfs object

	x = 0
	while x == 0:

		print("Randomly generated puzzle value: " + str(bfs.value))

		if bfs.value <= 0:
			print("This puzzle is UNSOLVABLE")


		userInput = raw_input("Type '1' for the puzzle board, '2' for the move depth of each position, '3' for the visited position matrix, '4' for a HillClimb mutation, 'q' to exit. ")

		if userInput == '1':
			draw.drawBoard(gameBoard.boardBuilt, gameBoard.boardSize)			# takes the created board and draws it with turtle, as visual output
			print("> Initial game board displayed.")
			print()

		elif userInput == '2':
			draw.drawBoard(bfs.steps, gameBoard.boardSize)
			print("> Number of steps to reach a position displayed.")
			print()

		elif userInput == '3':
			draw.drawBoard(bfs.visited, gameBoard.boardSize)
			print("> Visited tiles displayed.")
			print()

		elif userInput == '4':
			hc = HillClimb.HillClimb(gameBoard.boardBuilt, gameBoard.boardSize)
			gameBoard.boardBuilt = hc.mutate
			bfs = BFSearch.BFSearch(gameBoard.boardBuilt, gameBoard.boardSize)
			print("> HillClimb mutation.")
			print()

		elif userInput.lower() == 'q':
			quit()

		else:
			x = -1
#



if __name__ == "__main__":
	mainAT()
#
