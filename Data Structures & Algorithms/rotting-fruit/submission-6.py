class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        dq = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    dq.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        minutes = 0
        while fresh > 0 and dq:

            minutes += 1
            for _ in range(len(dq)):
                r, c = dq.popleft()
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or grid [nr][nc] != 1:
                            continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    dq.append((nr, nc))
        
        return minutes if fresh == 0 else -1
