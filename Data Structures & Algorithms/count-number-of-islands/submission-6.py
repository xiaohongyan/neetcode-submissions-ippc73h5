class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        cnt = 0

        dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dq = deque()
        
        def findIsland(r, c):
            dq = deque()
            dq.append([r, c])
            grid[r][c] = "#"

            while dq:
                r, c = dq.popleft()
                for d in dr:
                    new_r = r + d[0]
                    new_c = c + d[1]
                    if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] != "1":
                        continue
                    grid[new_r][new_c] = "#"
                    dq.append([new_r, new_c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    findIsland(r, c)
                    cnt += 1
        
        return cnt