# Anthony Tiongson
# Python 2.7

class HillClimb():

    def __init__(self, board, size):

# make an array to store the values of bfs.value as the board mutates through iterations,
# where the index of the array represents the iterative count
# board[random i in range(size)][random j in range(size)] = random legal value
        newBoard = board

        newBoard[0][0] = 1

        self.mutate = newBoard
