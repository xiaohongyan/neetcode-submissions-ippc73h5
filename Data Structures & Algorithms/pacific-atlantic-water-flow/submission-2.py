class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific, alantic = set(), set()

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        def dfs(r, c, visited, preHeight):

            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or heights[r][c] < preHeight:
                return

            visited.add((r, c))
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                dfs(nr, nc, visited, heights[r][c])


        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, alantic, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, alantic, heights[ROWS - 1][c])


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and  (r, c) in alantic:
                    res.append([r, c])

        return res


            


        