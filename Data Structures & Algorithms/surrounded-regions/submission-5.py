class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS = len(board)
        COLS = len(board[0])

        toOcean = set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            if board[r][c] != 'O' or (r, c) in toOcean:
                return
            
            dq = deque()
            dq.append((r, c))
            toOcean.add((r, c))

            while dq:
                i, j = dq.popleft()

                for d in directions:
                    nr = i + d[0]
                    nc = j + d[1]
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in toOcean or board[nr][nc]  !='O':
                        continue

                    dq.append((nr, nc))
                    toOcean.add((nr, nc))


        for r in range(ROWS):
            bfs(r, 0)
            bfs(r, COLS - 1)

        for c in range(COLS):
            bfs(0, c)
            bfs(ROWS - 1, c)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]  =='O' and (r, c) not in toOcean:
                    board[r][c]  ='X'
