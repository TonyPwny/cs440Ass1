# Thomas Fiorilla
# File specifically for project demo to TA

import matplotlib.pyplot as plt		# import class for making a plot
import board				# import code for creating the board
import draw					# import code for visually displaying the board on screen
import evaluate				# import code for bfs
import hill					# import code for hill-climbing

# Make two boards of the four default sizes
five1 = board.Board(5)
five2 = board.Board(5)

seven1 = board.Board(7)
seven2 = board.Board(7)

nine1 = board.Board(9)
nine2 = board.Board(9)

eleven1 = board.Board(11)
eleven2 = board.Board(11)

# Make a bfs object for each board generated
bfs1 = evaluate.evaluate(five1.boardBuilt, five1.boardSize)
bfs2 = evaluate.evaluate(five2.boardBuilt, five2.boardSize)

bfs3 = evaluate.evaluate(seven1.boardBuilt, seven1.boardSize)
bfs4 = evaluate.evaluate(seven2.boardBuilt, seven2.boardSize)

bfs5 = evaluate.evaluate(nine1.boardBuilt, nine1.boardSize)
bfs6 = evaluate.evaluate(nine2.boardBuilt, nine2.boardSize)

bfs7 = evaluate.evaluate(eleven1.boardBuilt, eleven1.boardSize)
bfs8 = evaluate.evaluate(eleven2.boardBuilt, eleven2.boardSize)

plt.plot([5, 5, 7, 7, 9, 9, 11, 11], [bfs1.evalTime, bfs2.evalTime, bfs3.evalTime, bfs4.evalTime, bfs5.evalTime, bfs6.evalTime, bfs7.evalTime, bfs8.evalTime], 'ro')
plt.xlabel("Size of board, 'n'")
plt.ylabel("Time (ms)")
plt.suptitle("Time to run BFS")
plt.show()
plt.clf()

# Create all 8 hill-climbing objects
hill1 = hill.Hill(five1)
hill2 = hill.Hill(five2)

hill3 = hill.Hill(seven1)
hill4 = hill.Hill(seven2)

hill5 = hill.Hill(nine1)
hill6 = hill.Hill(nine2)

hill7 = hill.Hill(eleven1)
hill8 = hill.Hill(eleven2)

# Iterate the hill-climb objects 50 times
hill1.climb(50)
hill2.climb(50)

hill3.climb(50)
hill4.climb(50)

hill5.climb(50)
hill6.climb(50)

hill7.climb(50)
hill8.climb(50)

# Plot the time it takes each hill function to run
plt.subplot(211)
plt.plot([5, 5, 7, 7, 9, 9, 11, 11], [hill1.evalTime, hill2.evalTime, hill3.evalTime, hill4.evalTime, hill5.evalTime, hill6.evalTime, hill7.evalTime, hill8.evalTime], 'ro')
plt.xlabel("Size of board, 'n'")
plt.ylabel("Time (ms)")

# Plot the increase in difficulty
plt.subplot(212)
plt.plot([5, 7, 9, 11], [hill1.score - bfs1.value, hill3.score - bfs3.value, hill5.score - bfs5.value, hill7.score - bfs7.value], 'bo')
plt.plot([5, 7, 9, 11], [hill2.score - bfs2.value, hill4.score - bfs4.value, hill6.score - bfs6.value, hill8.score - bfs8.value], 'go')
plt.xlabel("Size of board, 'n'")
plt.ylabel("Increase")

plt.suptitle("Time to increase difficullty, number difficulty increased by")
plt.show()
