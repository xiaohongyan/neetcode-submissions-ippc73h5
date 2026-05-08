class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
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
            self.Size[root_i] += self.Size[root_j]
            self.Parent[root_j] = root_i
        else:
            self.Size[root_j] += self.Size[root_i]
            self.Parent[root_i] = root_j
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        cnt = 0
        dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dsu = DSU(ROWS * COLS)  
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    cnt += 1
                    for d in dr:
                        new_r = r + d[0]
                        new_c = c + d[1]
                        if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] != "1":
                            continue

                        idx = r * COLS + c
                        new_idx = new_r * COLS + new_c
                        if dsu.union(idx, new_idx):
                            cnt -= 1
        return cnt
