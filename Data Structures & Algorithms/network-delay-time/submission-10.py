class Solution:
    #Dijkstra's algorithm
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        adj = defaultdict(list)

        visited = set()
        for u, v, w in times:
            adj[u].append((v, w))

        minHeap = [(0, k)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visited:
                continue

            visited.add(n1)
            for n2, w2 in adj[n1]:
                if n2 in visited:
                    continue

                if  dist[n2] >  dist[n1] + w2:
                     dist[n2] =  dist[n1] + w2
                     heapq.heappush(minHeap, (dist[n2], n2))
        

        return max(dist[1:]) if len(visited) == n else -1