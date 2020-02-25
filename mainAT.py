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

	eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)			# creates the BFS evaluate object
	AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)	# creates the A* evaluate object

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

			userInputHC = raw_input("\nEnter number of iterations to run a hill-climbing mutation: ")

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

				if eval2.value >= eval1.value:

					print('Hill-climbing mutation better or as good')
					puzzle = copy.deepcopy(newPuzzle)
					eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)
				else:

					print('Original puzzle better')
					eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)

				count += 1
				iterations -= 1

			print("\n> Hill-climbing mutation.\n")

		elif userInput == '6':

# Genetic Algorithm, forked from Hill-Climbing

			userInputGA = raw_input("\nEnter number of iterations to run a genetic mutation: ")

			iterations = int(userInputGA)

			n_max = puzzle.boardSize - 1
			puzzle_2 = copy.deepcopy(puzzle)
			puzzle_3 = copy.deepcopy(puzzle)
			puzzle_4 = copy.deepcopy(puzzle)
			count = 1

			while iterations > 0:

				print('Iteration: ' + str(count))

				AStarAgent1 = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)

				if AStarAgent1.value < 0:

					print("\nUsing a tweaked general hill-climbing mutation for UNSOLVABLE puzzle.\n")
					i_r = random.randint(0, n_max)

					if i_r == n_max:

						j_r = random.randint(0, (n_max - 1))
					else:

						j_r = random.randint(0, n_max)

					newMove = board.valid(i_r, j_r, puzzle.boardSize)
					same = True

					while same:

						if newMove != puzzle_2.boardBuilt[i_r][j_r]:

							puzzle_2.boardBuilt[i_r][j_r] = newMove
							same = False
							print("Successfully generated a different random.")
						else:

							newMove = board.valid(i_r, j_r, puzzle.boardSize)
							print("Same random, generating another...")

					AStarAgent2 = AStarEval.AStarEval(puzzle_2.boardBuilt, puzzle.boardSize)

					if AStarAgent2.value >= AStarAgent1.value:

						puzzle = copy.deepcopy(puzzle_2)
						AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
						print('General hill-climibing mutation better than/as good as original')
					else:

						AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
						print('Original puzzle better than general hill-climbing mutation')

				else:

					if eval.shortestPath != AStarAgent1.shortestPath:

						print("\nAt least 2 shortest paths detected. Targeting both and comparing results:\n")
						i_r, j_r = random.choice(eval.shortestPath[1:])
						print("Random (i, j) in BFS shortest path: (" + str(i_r) + ", " + str(j_r) + ")")
						i_ra, j_ra = random.choice(AStarAgent1.shortestPath[1:])
						same = True

						while same:

							if i_r == i_ra and j_r == j_ra:

								i_ra, j_ra = random.choice(AStarAgent1.shortestPath[1:])
							else:

								print("Random (i, j) in A* shortest path: (" + str(i_ra) + ", " + str(j_ra) + ")")
								same = False

						newMove = board.valid(i_r, j_r, puzzle.boardSize)
						newMove_a = board.valid(i_ra, j_ra, puzzle.boardSize)
						same = True

						while same:

							if newMove != puzzle_2.boardBuilt[i_r][j_r]:

								puzzle_2.boardBuilt[i_r][j_r] = newMove
								same = False
								print("Successfully generated a different random.")
							else:

								newMove = board.valid(i_r, j_r, puzzle.boardSize)
								print("Same random, generating another...")

						same = True

						while same:

							if newMove_a != puzzle_3.boardBuilt[i_ra][j_ra]:

								puzzle_3.boardBuilt[i_ra][j_ra] = newMove_a
								same = False
								print("Successfully generated a different random.")
							else:

								newMove_a = board.valid(i_ra, j_ra, puzzle.boardSize)
								print("Same random, generating another...")

						puzzle_4.boardBuilt[i_r][j_r] = newMove
						puzzle_4.boardBuilt[i_ra][j_ra] = newMove_a
						AStarAgent2 = AStarEval.AStarEval(puzzle_2.boardBuilt, puzzle.boardSize)
						AStarAgent3 = AStarEval.AStarEval(puzzle_3.boardBuilt, puzzle.boardSize)
						AStarAgent4 = AStarEval.AStarEval(puzzle_4.boardBuilt, puzzle.boardSize)

						if AStarAgent4.value >= AStarAgent3.value:

							print('Genetic mutation on both shortest paths better than/as good as genetic mutation on the A* shortest path')

							if AStarAgent4.value >= AStarAgent2.value:

								print('Genetic mutation on both shortest paths better than/as good as genetic mutation on the BFS shortest path')

								if AStarAgent4 >= AStarAgent1.value:

									puzzle = copy.deepcopy(puzzle_4)
									AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
									print('Genetic mutation on both shortest paths better than/as good as original')
								else:

									AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
									print('Original puzzle better than genetic mutation on the 2 shortest paths')
							else:

								print('Genetic mutation on the BFS shortest path better than genetic mutation on both shortest paths')

								if AStarAgent2.value >= AStarAgent1.value:

									puzzle = copy.deepcopy(puzzle_2)
									AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
									print('Genetic mutation on the BFS shortest path better than/as good as original')
								else:

									AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
									print('Original puzzle better than genetic mutation on the BFS shortest path')
						else:

							print('Genetic mutation on the A* shortest path better than genetic mutation on both shortest paths')

							if AStarAgent3.value >= AStarAgent2.value:

								print('Genetic mutation on the A* shortest path better than/as good as genetic mutation on the BFS shortest path')

								if AStarAgent3.value >= AStarAgent1.value:

									puzzle = copy.deepcopy(puzzle_3)
									AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
									print('Genetic mutation on the A* shortest path better than/as good as original')
								else:

									AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
									print('Original puzzle better than genetic mutation on the A* shortest path')
							else:

								print('Genetic mutation on the BFS shortest path better than genetic mutation on the A* shortest path')

								if AStarAgent2.value >= AStarAgent1.value:

									puzzle = copy.deepcopy(puzzle_2)
									AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
									print('Genetic mutation on the BFS shortest path better than/as good as original')
								else:

									AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
									print('Original puzzle better than genetic mutation on the BFS shortest path')
					else:

						print("\nOnly one shortest paths detected. Targeting it and comparing results:\n")
						i_r, j_r = random.choice(AStarAgent1.shortestPath[1:])
						newMove = board.valid(i_r, j_r, puzzle.boardSize)
						same = True

						while same:

							if newMove != puzzle_2.boardBuilt[i_r][j_r]:

								puzzle_2.boardBuilt[i_r][j_r] = newMove
								same = False
								print("Successfully generated a different random.")
							else:

								newMove = board.valid(i_r, j_r, puzzle.boardSize)
								print("Same random, generating another...")

						AStarAgent2 = AStarEval.AStarEval(puzzle_2.boardBuilt, puzzle.boardSize)

						i_r2 = random.randint(0, n_max)

						if i_r2 == n_max:

							j_r2 = random.randint(0, (n_max - 1))
						else:

							j_r2 = random.randint(0, n_max)

						newMove = board.valid(i_r2, j_r2, puzzle.boardSize)
						same = True

						while same:

							if newMove != puzzle_3.boardBuilt[i_r2][j_r2]:

								puzzle_3.boardBuilt[i_r2][j_r2] = newMove
								same = False
								print("Successfully generated a different random.")
							else:

								newMove = board.valid(i_r2, j_r2, puzzle.boardSize)
								print("Same random, generating another...")

						AStarAgent3 = AStarEval.AStarEval(puzzle_3.boardBuilt, puzzle.boardSize)

						if AStarAgent2.value >= AStarAgent1.value:

							print('Targeted hill-climbing mutation better than/as good as original')

							if AStarAgent3.value >= AStarAgent2.value:

								puzzle = copy.deepcopy(puzzle_3)
								AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
								print('General hill-climbing mutation better than/as good as targeted')
							else:

								puzzle = copy.deepcopy(puzzle_2)
								AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
								print('Targeted hill-climbing mutation better than general')
						else:

							print('Original puzzle better than targeted hill-climbing mutation')

							if AStarAgent3.value >= AStarAgent1.value:

								puzzle = copy.deepcopy(puzzle_3)
								AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
								print('General hill-climbing mutation better than/as good as original')
							else:

								AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
								print('Original puzzle better than general hill-climbing mutation')

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
