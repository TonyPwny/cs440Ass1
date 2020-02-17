# Anthony Tiongson fork from Fiorilla
# Python2.7

from queue import Queue

class BFSearch():
    def __init__(self, board, size):
        q = Queue()
        v = set()
        depth = 0

        self.visited = [['N' for i in range(size)] for j in range(size)]
        self.steps = [['X' for i in range(size)] for j in range(size)]

        q.put((0, 0, depth))
        v.add((0, 0))

        while not q.empty():
            i, j, d = q.get()

            m = board[i][j]
            self.visited[i][j] = 'Y'
            self.steps[i][j] = d
            for i_2, j_2 in ((i-m, j), (i+m, j), (i, j-m), (i, j+m)):

                if (0 <= i_2 < size) and (0 <= j_2 < size) and ((i_2, j_2) not in v):
                    q.put((i_2, j_2, self.steps[i][j] + 1))
                    v.add((i_2, j_2))
