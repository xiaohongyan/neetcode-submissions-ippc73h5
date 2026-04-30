class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        direction = [[-1, -1], [-1, 1], [-1, 0], [0, -1]] # only need 4 directions since it is processed from up to bottom and left to right

        def isValid(r, c):
            for d in direction:
                i, j = r, c

                while 0 <= i + d[0] < n and 0 <= j + d[1] < n:
                    i += d[0]
                    j += d[1]
                    if board[i][j] == 'Q':
                        return False
            return True
            
        def backtracking(row):

            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for col in range(n):
                if isValid(row, col):
                    board[row][col] = 'Q'
                    backtracking(row + 1)
                    board[row][col] = '.'

        backtracking(0)
        return res


        