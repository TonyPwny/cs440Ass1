# Anthony Tiongson fork from Fiorilla
# Python2.7

import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import copy
import random
import evaluate

def mainAT():
	userInput = raw_input("Enter 5 or greater for a board of that size, or 0 to randomize the board. ")

	puzzle = board.Board(userInput)											# builds a Board() object and assigns it to puzzle

	eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)		# creates the evaluate object

	x = 0
	while x == 0:

		print("Puzzle difficulty score: " + str(eval.value))

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

			userInputHC = raw_input("Enter number of iterations to run hill climbing mutation: ")

			iterations = int(userInputHC)

			n_max = puzzle.boardSize - 1
			newPuzzle = copy.deepcopy(puzzle)
			count = 1

			while iterations > 0:
				print('Iteration: ' + str(count))
				eval1 = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)

				newPuzzle.boardBuilt[0][0] = 1

				i_r = random.randint(0, n_max)

				if i_r == n_max:
					j_r = random.randint(0, (n_max - 1))
				else:
					j_r = random.randint(0, n_max)

				newPuzzle.boardBuilt[i_r][j_r] = board.valid(i_r, j_r, puzzle.boardSize)

				eval2 = evaluate.evaluate(newPuzzle.boardBuilt, puzzle.boardSize)

				if eval2.value > eval1.value:
					print('Hill Climbing mutation better')
					puzzle = copy.deepcopy(newPuzzle)
					eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)
				else:
					print('Original puzzle better or as good')
					eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)

				count += 1
				iterations -= 1

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
