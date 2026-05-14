class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        updated = True
        rounds = n - 1

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while rounds > 0 and updated:
            updated = False
            for u, v, t in times:
                if dist[v] > dist[u] + t:
                    dist[v] = dist[u] + t
                    updated = True
            rounds -= 1

        res =  max(dist[1:])
        return res if res < float('inf') else -1

            

        