class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if not n or not edges:
            return 0

        cnt = n
        dsu = DSU(n)

        for e in edges:
            p, q = e[0], e[1]
            if dsu.union(p, q):
                cnt -= 1

        return cnt

        