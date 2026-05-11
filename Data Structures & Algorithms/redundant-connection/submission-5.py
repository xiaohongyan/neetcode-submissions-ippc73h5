class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n+1)

    def find(self, i):
        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i])
        return  self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False

        if self.size[root_i] > self.size[root_j]:
            root_i, root_j = root_j, root_i
        
        self.size[root_j] += self.size[root_i]
        self.parent[root_i] = root_j
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        dsu = DSU(n)
        res = []

        for i, j in edges:
            if not dsu.union(i, j):
                res = [i, j]

        return res
        