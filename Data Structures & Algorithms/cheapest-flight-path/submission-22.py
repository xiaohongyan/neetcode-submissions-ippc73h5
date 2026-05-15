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
                if price[n2] > cost + w:  # 不能是 price[n1] + w, 因为price[n1] 是全局最优, 而不是当前步数下的最优
                    price[n2] = cost + w
                    dq.append((price[n2], n2, stop + 1))

        res = price[dst]

        return res if res < float('inf') else -1

            