class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.component = n

    def find(self, node):
        root = node
        while self.parent[root] != root:
            root = self.parent[root]
        
        while self.parent[node] != root:
            tmp = self.parent[node]
            self.parent[node] = root
            node = tmp
        return root
    
    def union(self, p, v):
        root_p = self.find(p)
        root_v = self.find(v)

        if root_p == root_v:
            return False

        if self.size[root_p] >= self.size[root_v]:
            root_p, root_v = root_v, root_p
        self.size[root_v] += self.size[root_p]
        self.parent[root_p] = root_v
        self.component -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n -1:
            return False
            
        dsu = DSU(n)

        for p, v in edges:
            if not dsu.union(p, v):    
                return False

        return dsu.component == 1


        