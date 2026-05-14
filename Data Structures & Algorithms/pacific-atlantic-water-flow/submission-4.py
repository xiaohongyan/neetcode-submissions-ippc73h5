class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific, alantic = set(), set()

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        
        def bfs(r, c, visited):

            if (r, c) in visited:
                return

            dq = deque()
            dq.append((r, c))
            visited.add((r, c))

            while dq:
                i, j = dq.popleft()
                for d in directions:
                    nr = i + d[0]
                    nc = j + d[1]
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or heights[nr][nc] < heights[i][j]:
                        continue
                    dq.append((nr, nc))
                    visited.add((nr, nc))

        for r in range(ROWS):
            bfs(r, 0, pacific)
            bfs(r, COLS - 1, alantic)

        for c in range(COLS):
            bfs(0, c, pacific)
            bfs(ROWS - 1, c, alantic)


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and  (r, c) in alantic:
                    res.append([r, c])

        return res


            


        