'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
'''
# when live, if count < 2 or count > 3, change state, board[i][j] = 2 
# when die, if count == 3, change state, board[i][j] = 2
# board[i][j] %= 2 
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dx = [-1,-1,0,1,1,1,0,-1]
        dy = [0,1,1,1,0,-1,-1,-1]
        if len(board) == 0 or len(board[0]) == 0: return
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and (board[x][y] == 1 or board[x][y] == 2):
                        count += 1
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 2
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 3
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j] % 2
