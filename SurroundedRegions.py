__author__ = 'WangZhe'
from collections import deque


class Board(object):

    def __init__(self, board):
        self.board = board
        self.explored = set()
        self.max_y = len(board) - 1
        self.max_x = len(board[0]) - 1 if self.max_y >= 0 else -1

    def BFS(self, i, j):
        queue = deque([(i, j)])
        self.explored.add((i, j))

        while len(queue) != 0:
            i, j = queue.popleft()
            left = max(0, j - 1)
            right = min(j + 1, self.max_x)
            up = max(0, i - 1)
            down = min(self.max_y, i + 1)

            x = left
            y = i
            if (y, x) not in self.explored and self.board[y][x] == 'O':
                self.explored.add((y, x))
                queue.append((y, x))

            x = right
            y = i
            if (y, x) not in self.explored and self.board[y][x] == 'O':
                self.explored.add((y, x))
                queue.append((y, x))

            x = j
            y = up
            if (y, x) not in self.explored and self.board[y][x] == 'O':
                self.explored.add((y, x))
                queue.append((y, x))

            x = j
            y = down
            if (y, x) not in self.explored and self.board[y][x] == 'O':
                self.explored.add((y, x))
                queue.append((y, x))

    def flip(self):
        for i in range(self.max_y + 1):
            for j in range(self.max_x + 1):
                if self.board[i][j] == 'O' and (i, j) not in self.explored:
                    self.board[i][j] = 'X'


class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        #if len(board) == 0:
        #    return []
        bd = Board(board)
        if bd.max_y >= 2 and bd.max_x >= 2:
            for i in range(bd.max_x + 1):
                if board[0][i] == 'O':
                    bd.BFS(0, i)
                if board[bd.max_y][i] == 'O':
                    bd.BFS(bd.max_y, i)
            for j in range(bd.max_y + 1):
                if board[j][0] == 'O':
                    bd.BFS(j, 0)
                if board[j][bd.max_x] == 'O':
                    bd.BFS(j, bd.max_x)
            bd.flip()

        return bd.board







if __name__ == '__main__':
    board = [
        ['X', 'X', 'X'],
        ['X', 'O', 'X'],
        ['X', 'X', 'X'],

    ]

    print(Solution().solve(board))