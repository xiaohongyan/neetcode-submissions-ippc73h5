class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        cols = set()
        main_diag = set()
        anti_diag = set()
        
        def backtracking(row):

            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for col in range(n):
                if col in cols or row - col in main_diag or row + col in anti_diag:
                    continue

                cols.add(col)
                main_diag.add(row - col)
                anti_diag.add(row + col)
                board[row][col] = 'Q'

                backtracking(row + 1)

                cols.remove(col)
                main_diag.remove(row - col)
                anti_diag.remove(row + col)
                board[row][col] = '.'

        backtracking(0)
        return res


        