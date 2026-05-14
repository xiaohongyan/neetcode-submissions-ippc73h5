class Solution:
    # Shortest Path Faster Algorithm
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dq = deque()
        dq.append(k)
        while dq:
            n1 = dq.popleft()
            for n2, w in adj[n1]:
                if dist[n2] > dist[n1] + w:
                    dist[n2] = dist[n1] + w
                    dq.append(n2)


        res =  max(dist[1:])
        return res if res < float('inf') else -1