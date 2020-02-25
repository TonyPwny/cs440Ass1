# Thomas Fiorilla
# File specifically for project demo to TA

import matplotlib.pyplot as plt		# import class for making a plot
import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import evaluate				# import code for bfs
import hill					# import code for hill-climbing
import AStarEval			# import code for A* search
import genetic				# import code for genetic algorithm

size = 16										# size of the array
numberPer = size/4								# with default 4 'n' sizes, number of sizes of each 'n'
boards = [None for x in range(size)]			# array for 'size' board ojects

hills = [None for x in range(size)]				# array for hill-climbing objects to make a more difficult board

gene = [None for x in range(size)]				# array for genetic algorithm objects

bfs = [None for x in range(size)]				# array for the BFS objects evaluating the original board
bfsHill = [None for x in range(size)]			# array for the BFS objects evaluating the hill-climbing board

aStar = [None for x in range(size)]				# array for the A* objects evaluating the original board
aStarHill = [None for x in range(size)]			# array for the A* objects evaluating the hill-climbing board



sizeArray = [None for x in range(size)]			# holds the 'n' sizes at their proper indices
iterations = 100								# number of iterations for hill climbing

markers = ["o", "v" , "^" , "<", ">", "o", "v" , "^" , "<", ">"]
colors = ['r','g','b','c','m', 'y', 'k', 'pink']

i = 0
j = 0
n = 5
# Make numberPer amount of boards of the four default sizes, create bfs objects for all of them, make hill-climbing objects for all of them, then iterate each object 50 times
while i < size:
	while  j < numberPer:
		boards[i] = board.Board(n)
		
		hills[i] = hill.Hill(boards[i])													# create hill-climbing objects
		hills[i].climb(iterations)														# iterate hill-climbing objects
		
		bfs[i] = evaluate.evaluate(boards[i].boardBuilt, boards[i].boardSize)					# create BFS objects to evaluate original board
		bfsHill[i] = evaluate.evaluate(hills[i].puzzle.boardBuilt, hills[i].puzzle.boardSize)	# create BFS object to evaluate hill-climbing board
		
		gene[i] = genetic.Genetic(boards[i])
		gene[i].run(bfs[i], iterations)
		
		aStar[i] = AStarEval.AStarEval(boards[i].boardBuilt, boards[i].boardSize)					# create A* objects to evaluate original board
		aStarHill[i] = AStarEval.AStarEval(hills[i].puzzle.boardBuilt, hills[i].puzzle.boardSize)	# create A* objects to evaluate hill-climbing board
		
		sizeArray[i] = n
		
		i += 1
		j += 1
	
	n += 2
	j = 0

bfsScore = [n.value for n in bfs]								# array with the bfs scores
bfsTime = [n.evalTime for n in bfs]								# array with the bfs time evaluation

bfsTimeHill = [n.evalTime for n in bfsHill]

geneTime = [n.evalTime for n in gene]							# array with genetic algorithm time evaluation
geneScore = [n.score for n in gene]								# 

hillScore = [n.score for n in hills]							# array with the hill-climb scores
hillTime = [n.evalTime for n in hills]							# array with the hill-climb time evaluation

scoreDif = [i - j for i, j in zip(hillScore, bfsScore)]			# array with the difference between new score and original score
geneDif = [i - j for i, j in zip(geneScore, bfsScore)]			# 

aTime = [n.evalTime for n in aStar]								# array with the evaluation times for A*, original board
aTimeHill = [n.evalTime for n in aStarHill]						# array with the evaluation times for A*, hill-climb board



# Function to plot running time for the bfs
def plotBFS():
	plt.subplot(121)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], bfsTime[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each BFS")
	
	# Plot showing the score of each puzzle
	plt.subplot(122)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], bfsScore[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Score")
	plt.title("Score of each board")
	
	plt.suptitle("Data for Breadth-First-Search")
	
	plt.show()
	plt.clf()



# Function to plot the running time for each hill-climb
def plotHill():
	plt.subplot(221)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], hillTime[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each set of iterations")
	
	# Plot the increase in difficulty
	plt.subplot(222)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], scoreDif[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Score")
	plt.title("Increase in score")
	
	# Plot the original score
	plt.subplot(223)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], bfsScore[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Score")
	plt.title("Original score")
	
	# Plot the ending score
	plt.subplot(224)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], hillScore[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Score")
	plt.title("New score")
	
	plt.suptitle("Data for " + str(iterations) + " hill-climbing iterations")
	
	plt.show()
	plt.clf()



# Plot runtime of BFS vs runtime of A*
def plotComp():
	plt.subplot(221)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], bfsTime[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each BFS, original")
	
	# 
	plt.subplot(222)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], aTime[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each A*, original")
	
	#
	plt.subplot(223)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], bfsTimeHill[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each BFS, hill-climb")
	
	# 
	plt.subplot(224)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], aTimeHill[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each A*, hill-climb")
	
	plt.suptitle("BFS vs A* for Time")
	
	plt.show()
	plt.clf()



# Plot average runtime of BFS vs average runtime of A*
def plotCompAverage():
	plt.subplot(221)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], bfsTime[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each BFS, original")
	
	# 
	plt.subplot(222)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], aTime[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each A*, original")
	
	#
	plt.subplot(223)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], bfsTimeHill[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each BFS, hill-climb")
	
	# 
	plt.subplot(224)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], aTimeHill[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each A*, hill-climb")
	
	plt.suptitle("BFS vs A* for Time")
	
	plt.show()
	plt.clf()
	


def plotGene():
	plt.subplot(221)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], geneTime[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Time (ms)")
	plt.title("Time for each set of iterations")
	
	# Plot the increase in difficulty
	plt.subplot(222)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], geneDif[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Score")
	plt.title("Increase in score")
	
	# Plot the original score
	plt.subplot(223)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], bfsScore[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Score")
	plt.title("Original score")
	
	# Plot the ending score
	plt.subplot(224)
	i = 0
	while i < int(numberPer):
		plt.plot(sizeArray[i::int(numberPer)], geneScore[i::int(numberPer)], color = colors[i], marker = markers[i], linestyle = 'none')
		i += 1
	plt.xlabel("Size of board, 'n'")
	plt.ylabel("Score")
	plt.title("New score")
	
	plt.suptitle("Data for " + str(iterations) + " genetic algorithm iterations")
	
	plt.show()
	plt.clf()



# Create loop for user input
while True:
	print()
	userInput = input("Type '1' for BFS data, '2' for hill-climbing data, '3' to compare BFS to A*, '4' for genetic data, 'q' to exit. ")
	
	if userInput == '1':
		print("> BFS data displayed.")
		print("> Time; " + str(bfsTime))
		print("> Scores: " + str(bfsScore))
		plotBFS()
	
	elif userInput == '2':
		print("> Hill-climbing data displayed.")
		print("> Time; " + str(hillTime))
		print("> Scores: " + str(hillScore))
		plotHill()
	
	elif userInput == '3':
		print("> BFS vs A* displayed.")
		#print("> BFS time; " + str(bfsTime))
		#print("> A* time: " + str(aTime))
		plotComp()
	
	elif userInput == '4':
		print("> Genetic algorithm data displayed.")
		print("> Time; " + str(geneTime))
		print("> Scores: " + str(geneScore))
		plotGene()
	
	elif userInput == 'q':
		break
