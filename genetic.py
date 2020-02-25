# Thomas Fiorilla, fork of Anthony Tiongson
# Anthony's genetic algorithm turned into a class

import AStarEval
import random


iterations = int(userInputHC)

n_max = puzzle.boardSize - 1
puzzle_2 = copy.deepcopy(puzzle)
puzzle_3 = copy.deepcopy(puzzle)
puzzle_4 = copy.deepcopy(puzzle)
count = 1

while iterations > 0:

	#print('Iteration: ' + str(count))

	AStarAgent1 = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)

	if AStarAgent1.value < 0:

		#print("\nUsing tweaked general hill-climbing mutation for UNSOLVABLE puzzle.\n")
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
				#print("Successfully generated a different random.")
			else:

				newMove = board.valid(i_r, j_r, puzzle.boardSize)
				#print("Same random, generating another...")

		AStarAgent2 = AStarEval.AStarEval(puzzle_2.boardBuilt, puzzle.boardSize)

		if AStarAgent2.value >= AStarAgent1.value:

			puzzle = copy.deepcopy(puzzle_2)
			AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
			#print('General hill-climibing mutation better than/as good as original')
		else:

			AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
			#print('Original puzzle better than general hill-climbing mutation on the BFS shortest path')

	else:

		if eval.shortestPath != AStarAgent1.shortestPath:

			#print("\nAt least 2 shortest paths detected. Targeting both and comparing results:\n")
			i_r, j_r = random.choice(eval.shortestPath[1:])
			#print("Random (i, j) in BFS shortest path: (" + str(i_r) + ", " + str(j_r) + ")")
			i_ra, j_ra = random.choice(AStarAgent1.shortestPath[1:])
			same = True

			while same:

				if i_r == i_ra and j_r == j_ra:

					i_ra, j_ra = random.choice(AStarAgent1.shortestPath[1:])
				else:

					#print("Random (i, j) in A* shortest path: (" + str(i_ra) + ", " + str(j_ra) + ")")
					same = False

			newMove = board.valid(i_r, j_r, puzzle.boardSize)
			newMove_a = board.valid(i_ra, j_ra, puzzle.boardSize)
			same = True

			while same:

				if newMove != puzzle_2.boardBuilt[i_r][j_r]:

					puzzle_2.boardBuilt[i_r][j_r] = newMove
					same = False
					#print("Successfully generated a different random.")
				else:

					newMove = board.valid(i_r, j_r, puzzle.boardSize)
					#print("Same random, generating another...")

			same = True

			while same:

				if newMove_a != puzzle_3.boardBuilt[i_ra][j_ra]:

					puzzle_3.boardBuilt[i_ra][j_ra] = newMove_a
					same = False
					#print("Successfully generated a different random.")
				else:

					newMove_a = board.valid(i_ra, j_ra, puzzle.boardSize)
					#print("Same random, generating another...")

			puzzle_4.boardBuilt[i_r][j_r] = newMove
			puzzle_4.boardBuilt[i_ra][j_ra] = newMove_a
			AStarAgent2 = AStarEval.AStarEval(puzzle_2.boardBuilt, puzzle.boardSize)
			AStarAgent3 = AStarEval.AStarEval(puzzle_3.boardBuilt, puzzle.boardSize)
			AStarAgent4 = AStarEval.AStarEval(puzzle_4.boardBuilt, puzzle.boardSize)

			if AStarAgent4.value >= AStarAgent3.value:

				#print('Genetic mutation on both shortest paths better than/as good as genetic mutation on the A* shortest path')

				if AStarAgent4.value >= AStarAgent2.value:

					#print('Genetic mutation on both shortest paths better than/as good as genetic mutation on the BFS shortest path')

					if AStarAgent4 >= AStarAgent1.value:

						puzzle = copy.deepcopy(puzzle_4)
						AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
						#print('Genetic mutation on both shortest paths better than/as good as original')
					else:

						AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
						#print('Original puzzle better than genetic mutation on the 2 shortest paths')
				else:

					#print('Genetic mutation on the BFS shortest path better than genetic mutation on both shortest paths')

					if AStarAgent2.value >= AStarAgent1.value:

						puzzle = copy.deepcopy(puzzle_2)
						AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
						#print('Genetic mutation on the BFS shortest path better than/as good as original')
					else:

						AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
						#print('Original puzzle better than genetic mutation on the BFS shortest path')
			else:

				#print('Genetic mutation on the A* shortest path better than genetic mutation on both shortest paths')

				if AStarAgent3.value >= AStarAgent2.value:

					#print('Genetic mutation on the A* shortest path better than/as good as genetic mutation on the BFS shortest path')

					if AStarAgent3.value >= AStarAgent1.value:

						puzzle = copy.deepcopy(puzzle_3)
						AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
						#print('Genetic mutation on the A* shortest path better than/as good as original')
					else:

						AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
						#print('Original puzzle better than genetic mutation on the A* shortest path')
				else:

					#print('Genetic mutation on the BFS shortest path better than genetic mutation on the A* shortest path')

					if AStarAgent2.value >= AStarAgent1.value:

						puzzle = copy.deepcopy(puzzle_2)
						AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
						#print('Genetic mutation on the BFS shortest path better than/as good as original')
					else:

						AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
						#print('Original puzzle better than genetic mutation on the BFS shortest path')
		else:

			#print("\nOnly one shortest paths detected. Targeting it and comparing results:\n")
			i_r, j_r = random.choice(AStarAgent1.shortestPath[1:])
			newMove = board.valid(i_r, j_r, puzzle.boardSize)
			same = True

			while same:

				if newMove != puzzle_2.boardBuilt[i_r][j_r]:

					puzzle_2.boardBuilt[i_r][j_r] = newMove
					same = False
					#print("Successfully generated a different random.")
				else:

					newMove = board.valid(i_r, j_r, puzzle.boardSize)
					#print("Same random, generating another...")

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
					#print("Successfully generated a different random.")
				else:

					newMove = board.valid(i_r2, j_r2, puzzle.boardSize)
					#print("Same random, generating another...")

			AStarAgent3 = AStarEval.AStarEval(puzzle_3.boardBuilt, puzzle.boardSize)

			if AStarAgent2.value >= AStarAgent1.value:

				#print('Targeted hill-climbing mutation better than/as good as original')

				if AStarAgent3.value > AStarAgent2.value:

					puzzle = copy.deepcopy(puzzle_3)
					AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
					#print('General hill-climbing mutation better than targeted')
				else:

					puzzle = copy.deepcopy(puzzle_2)
					AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
					#print('Targeted hill-climbing mutation better than general')
			else:

				#print('Original puzzle better than targeted hill-climbing mutation')

				if AStarAgent3.value >= AStarAgent1.value:

					puzzle = copy.deepcopy(puzzle_3)
					AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
					#print('General hill-climbing mutation better than/as good as original')
				else:

					AStarAgent = AStarEval.AStarEval(puzzle.boardBuilt, puzzle.boardSize)
					#print('Original puzzle better than general hill-climbing mutation')

	eval = evaluate.evaluate(puzzle.boardBuilt, puzzle.boardSize)
	count += 1
	iterations -= 1
