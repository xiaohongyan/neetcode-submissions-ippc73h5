class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1)) #[0, 1, 2, ..., n]
        self.Size = [1] * (n + 1)
    
    def find(self,i):
        if self.Parent[i] == i:
            return i
        
        self.Parent[i] = self.find(self.Parent[i])
        return self.Parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False
        if self.Size[root_i] >= self.Size[root_j]:
            root_i, root_j = root_j, root_i

        self.Size[root_j] += self.Size[root_i]
        self.Parent[root_i] = root_j
        return True

    def getSize(self, i):
        root_i = self.find(i)
        return self.Size[root_i]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        dr = [[1, 0], [0, 1]]
        dsu = DSU(ROWS * COLS)
        max_area = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                idx = r * COLS + c
                if grid[r][c] == 1:
                    idx = r * COLS + c
                    for d in dr:
                        new_r = r + d[0]
                        new_c = c + d[1]
                        if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] != 1:
                            continue

                        new_idx = new_r * COLS + new_c
                        dsu.union(idx, new_idx)
                        
                    max_area = max(max_area,dsu.getSize(idx))
        return  max_area
