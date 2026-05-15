class Solution:
    # SPFA
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        price = [float('inf')] * n
        price[src] = 0

        adj = defaultdict(list)

        for f, t, p in flights:
            adj[f].append((t, p))

        dq = deque()
        dq.append((0, src, 0))

        while dq:
            cost, n1, stop = dq.popleft()

            if stop > k:
                continue

            for n2, w in adj[n1]:
                if price[n2] > cost + w:
                    price[n2] = cost + w
                    dq.append((price[n2], n2, stop + 1))

        res = price[dst]

        return res if res < float('inf') else -1

            