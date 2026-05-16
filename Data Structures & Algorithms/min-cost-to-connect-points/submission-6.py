class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

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
    # Kruskal
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        edges = []
        minHeap = []

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        heapq.heapify(edges)

        edge_cnt = 0
        dsu = DSU(n)
        res = 0
        while edge_cnt < n - 1 and edges:
            dist, i, j = heapq.heappop(edges)
            if dsu.union(i, j):
                 edge_cnt += 1
                 res += dist
        
        return res
            