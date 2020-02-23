# Anthony Tiongson forked from Thomas Fiorilla's main
# Python2.7

import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import copy
import random
import evaluate
import AStarEval

def mainAT():

	userInput = raw_input("\nEnter 5 or greater for a board of that size, or 0 to randomize the board: ")

	if userInput == "":
		userInput = 0

	puzzle = board.Board(userInput)											# builds a Board() object and assigns it to puzzle

	eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)		# creates the evaluate object

	while True:

		print("\nPuzzle difficulty score: " + str(eval.value))

		if eval.value < 0:

			print("This puzzle is UNSOLVABLE!\n")
		else:

			print("Path to goal:")
			print(eval.shortestPath[::-1])
			print("\n")



		userInput = raw_input("'1' for the puzzle board\n'2' for the move depth of each position\n'3' for the visited position matrix\n'4' for A* evaluation\n'5' for a HillClimb mutation\n'6' for a Genetic mutation\n'q' to exit\n\n>> ")

		if userInput == '1':

			draw.drawBoard(puzzle.boardBuilt, puzzle.boardSize)			# takes the created board and draws it with turtle, as visual output
			print("\n> Displaying puzzle.\n")

		elif userInput == '2':

			draw.drawBoard(eval.steps, puzzle.boardSize)
			print("\n> Displaying number of moves to reach each position.\n")

		elif userInput == '3':

			draw.drawBoard(eval.visited, puzzle.boardSize)
			print("\n> Displaying visitable positions.\n")

		elif userInput == '4':

			AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)

			while True:

				if AStarAgent.value < 0:

					print("\nSolvability score: " + str(AStarAgent.value))
					print("This puzzle is UNSOLVABLE!\n")
				else:

					print("\nA* evaluation solved in: " + str(AStarAgent.value) + " moves")
					print("Path to goal:")
					print(AStarAgent.shortestPath[::-1])
					print("\n")

				userInput = raw_input("\n'1' for the puzzle board\n'2' for the A* move depth evaluation\n'3' for the A* visited position matrix\n'b' to go back\n\n>> ")

				if userInput == '1':

					draw.drawBoard(puzzle.boardBuilt, puzzle.boardSize)			# takes the created board and draws it with turtle, as visual output
					print("\n> Displaying puzzle.\n")

				elif userInput == '2':

					draw.drawBoard(AStarAgent.steps, puzzle.boardSize)
					print("\n> Displaying A* move count for positions visited.\n")

				elif userInput == '3':

					draw.drawBoard(AStarAgent.visited, puzzle.boardSize)
					print("\n> Displaying positions visited by A* evaluation.\n")

				elif userInput == 'b':

					break

				elif userInput == 'q':

					quit()

				else:

					break

		elif userInput == '5':

			userInputHC = raw_input("\nEnter number of iterations to run a hill climbing mutation: ")

			iterations = int(userInputHC)

			n_max = puzzle.boardSize - 1
			newPuzzle = copy.deepcopy(puzzle)
			count = 1

			while iterations > 0:

				print('Iteration: ' + str(count))

				eval1 = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)
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

			print("\n> HillClimb mutation.\n")

		elif userInput == '6':

			userInputHC = raw_input("\nEnter number of iterations to run a genetic mutation: ")

			iterations = int(userInputHC)

			n_max = puzzle.boardSize - 1
			newPuzzle = copy.deepcopy(puzzle)
			count = 1

			while iterations > 0:

				print('Iteration: ' + str(count))

				AStarAgent1 = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
				i_r = random.randint(0, n_max)

				if i_r == n_max:

					j_r = random.randint(0, (n_max - 1))
				else:

					j_r = random.randint(0, n_max)

				newPuzzle.boardBuilt[i_r][j_r] = board.valid(i_r, j_r, puzzle.boardSize)

				AStarAgent2 = AStarEval.AStarEval(newPuzzle.boardBuilt, puzzle.boardSize)

				if AStarAgent2.value > AStarAgent1.value:

					print('Genetic mutation better')
					puzzle = copy.deepcopy(newPuzzle)
					eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)
				else:

					print('Original puzzle better or as good')
					eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)

				count += 1
				iterations -= 1

			print("\n> Genetic mutation.\n")

		elif userInput.lower() == 'q':

			quit()

		else:
			break
#



if __name__ == "__main__":
	mainAT()
#
