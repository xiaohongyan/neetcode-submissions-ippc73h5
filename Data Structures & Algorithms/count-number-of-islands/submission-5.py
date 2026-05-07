class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        cnt = 0
        
        def findIsland(r, c):

            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != "1":
                return

            grid[r][c] = "#"
            findIsland(r + 1, c)
            findIsland(r, c + 1)
            findIsland(r - 1, c)
            findIsland(r, c - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    findIsland(r, c)
                    cnt += 1
        

        return cnt
            

            



