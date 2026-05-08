class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        dr = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if r < 0 or c < 0  or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1
            for d in dr:
                new_r, new_c = r + d[0], c + d[1]
                area += dfs(new_r, new_c)
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
                
        return max_area

        