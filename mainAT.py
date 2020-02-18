# Anthony Tiongson fork from Fiorilla
# Python2.7

import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import evaluate

def mainAT():
	puzzle = board.Board()											# builds a Board() object and assigns it to puzzle

	eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)		# creates the evaluate object

	x = 0
	while x == 0:

		print("Randomly generated puzzle value: " + str(eval.value))

		if eval.value <= 0:
			print("This puzzle is UNSOLVABLE")


		userInput = raw_input("Type '1' for the puzzle board, '2' for the move depth of each position, '3' for the visited position matrix, '4' for a HillClimb mutation, 'q' to exit. ")

		if userInput == '1':
			draw.drawBoard(puzzle.boardBuilt, puzzle.boardSize)			# takes the created board and draws it with turtle, as visual output
			print("> Initial puzzle displayed.")
			print()

		elif userInput == '2':
			draw.drawBoard(eval.steps, puzzle.boardSize)
			print("> Number of steps to reach a position displayed.")
			print()

		elif userInput == '3':
			draw.drawBoard(eval.visited, puzzle.boardSize)
			print("> Visited tiles displayed.")
			print()

		elif userInput == '4':
			newPuzzle = eval.mutate(puzzle.boardBuilt, puzzle.boardSize)
			eval = evaluate.evaluate(newPuzzle, puzzle.boardSize)
			draw.drawBoard(newPuzzle, puzzle.boardSize)
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
