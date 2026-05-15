class Solution:
    #Dijkstra's algorithm
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        minHeap = [(0, k)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if dist[n1] < w1:
                continue

            for n2, w2 in adj[n1]:
                if dist[n2] < w2:
                    continue

                if  dist[n2] > w1 + w2:
                     dist[n2] = w1 + w2
                     heapq.heappush(minHeap, (dist[n2], n2))
        
        res = max(dist[1:])

        return res if res != float('inf') else -1