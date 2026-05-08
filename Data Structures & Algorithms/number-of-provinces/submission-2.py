class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.component = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False
        
        self.component -= 1
        if self.size[root_i] >= self.size[root_j]:
            root_i, root_j = root_j, root_i

        self.size[root_j] += self.size[root_i]
        self.parent[root_i] = root_j

        return True
    
    def getComponent(self):
        return self.component

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        dsu = DSU(n)
        for r in range(n):
            for c in range(r):
                if isConnected[r][c] == 1:
                    dsu.union(r, c)

        return dsu.getComponent()
        
