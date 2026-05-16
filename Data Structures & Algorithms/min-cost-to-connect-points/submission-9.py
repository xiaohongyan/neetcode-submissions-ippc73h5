class Solution:
    # Prime
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        minHeap = [(0, 0)]
        visited = set()
        res = 0
        while len(visited) < n:

            dist, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            res += dist
            for nei in range(n):
                if nei in visited:
                    continue
                x1, y1 = points[node]
                x2, y2 = points[nei]
                d = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minHeap, (d, nei))
       
        return res
        