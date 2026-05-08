class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        dr = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(r, c):
            dq = deque()
            dq.append([r, c])
            grid[r][c] = 0
            area = 1


            while dq:
                i, j = dq.popleft()
                

                for d in dr:
                    new_r, new_c = i + d[0], j + d[1]
                    if new_r < 0 or new_c < 0  or new_r == ROWS or new_c == COLS or grid[new_r][new_c] == 0:
                        continue

                    dq.append([new_r, new_c])
                    grid[new_r][new_c] = 0
                    area += 1

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
                
        return max_area