class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        WALL = 2147483647
        dq = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dq.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while dq:
                r, c = dq.popleft()
                for d in directions:
                        nr = r + d[0]
                        nc = c + d[1]
                        if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or grid [nr][nc] == -1 or grid [nr][nc] != WALL:
                                continue
                        
                        grid[nr][nc] =  grid[r][c] + 1
                        dq.append((nr, nc))
