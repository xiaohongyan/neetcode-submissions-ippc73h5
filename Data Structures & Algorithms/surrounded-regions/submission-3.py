class Solution:
    def solve(self, board: List[List[str]]) -> None:


        res = []
        ROWS = len(board)
        COLS = len(board[0])

        toOcean = set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c, toOcean):

            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in toOcean or board[r][c]  !='O':
                return

            toOcean.add((r, c))
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                dfs(nr, nc, toOcean)


        for r in range(ROWS):
            dfs(r, 0, toOcean)
            dfs(r, COLS - 1,toOcean)

        for c in range(COLS):
            dfs(0, c, toOcean)
            dfs(ROWS - 1, c, toOcean)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]  =='O' and (r, c) not in toOcean:
                    board[r][c]  ='X'
