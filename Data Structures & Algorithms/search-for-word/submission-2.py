class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        direction = [[0,1], [0,-1], [1, 0], [-1, 0]]

        def backtracking(r, c, i):

            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or visited[r][c] or board[r][c] != word[i]:
                return False

            visited[r][c] = True
            for d in direction:
                if backtracking(r + d[0], c + d[1], i + 1):
                    return True
            
            visited[r][c] = False

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if backtracking(row, col, 0): # find the starting of the str in the board
                        return True
        
        return False