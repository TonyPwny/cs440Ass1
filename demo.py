# Thomas Fiorilla
# File specifically for project demo to TA

import matplotlib.pyplot as plt		# import class for making a plot
import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import evaluate				# import code for bfs
import hill					# import code for hill-climbing

size = 8										# size of the array
numberPer = size/4								# with default 4 'n' sizes, number of sizes of each 'n'
boards = [None for x in range(size)]			# array for 'size' board ojects
bfs = [None for x in range(size)]				# array for 'size' bfs objects
hills = [None for x in range(size)]				# array for 'size' hill-climbing objects
sizeArray = [None for x in range(size)]			# holds the 'n' sizes at their proper indices

i = 0
j = 0
n = 5
# Make numberPer amount of boards of the four default sizes, create bfs objects for all of them, make hill-climbing objects for all of them, then iterate each object 50 times
while i < size:
	while  j < numberPer:
		boards[i] = board.Board(n)
		
		bfs[i] = evaluate.evaluate(boards[i].boardBuilt, boards[i].boardSize)
		
		hills[i] = hill.Hill(boards[i])
		hills[i].climb(50)
		
		sizeArray[i] = n
		
		i += 1
		j += 1
	
	n += 2
	j = 0

bfsScore = [n.value for n in bfs]								# array with the bfs scores
bfsTime = [n.evalTime for n in bfs]								# array with the bfs time evaluation
hillScore = [n.score for n in hills]							# array with the hill-climb scores
hillTime = [n.evalTime for n in hills]							# array with the hill-climb time evaluation
scoreDif = [i - j for i, j in zip(hillScore, bfsScore)]			# array with the difference between new score and original score

# Plot running time for the bfs
plt.plot(sizeArray[0::int(numberPer)], bfsTime[0::int(numberPer)], 'ro')
plt.plot(sizeArray[1::int(numberPer)], bfsTime[1::int(numberPer)], 'bo')
plt.xlabel("Size of board, 'n'")
plt.ylabel("Time (ms)")
plt.suptitle("Time to run BFS")
plt.show()
plt.clf()

# Plot the running time for each hill-climb
plt.subplot(211)
plt.plot(sizeArray[0::int(numberPer)], hillTime[0::int(numberPer)], 'ro')
plt.plot(sizeArray[1::int(numberPer)], hillTime[1::int(numberPer)], 'bo')
plt.xlabel("Size of board, 'n'")
plt.ylabel("Time (ms)")

# Plot the increase in difficulty
plt.subplot(212)
plt.plot(sizeArray[0::int(numberPer)], scoreDif[0::int(numberPer)], 'ro')
plt.plot(sizeArray[1::int(numberPer)], scoreDif[1::int(numberPer)], 'bo')
plt.xlabel("Size of board, 'n'")
plt.ylabel("Increase")

plt.suptitle("Time to increase difficullty, number difficulty increased by")
plt.show()
