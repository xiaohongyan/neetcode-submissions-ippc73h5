class Solution:
    # bfs
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for e in edges:
            u, v = e[0], e[1]
            adj[u].append(v)
            adj[v].append(u)

        cnt = 0
        def bfs(i):
            dq = deque()
            visited[i] = True
            dq.append(i)

            while dq:
                cur = dq.popleft()
                adjNode = adj[cur]
                for node in adjNode:
                    if visited[node]:
                        continue

                    visited[node] = True
                    dq.append(node)

        for i in range(n):
            if visited[i]:
                continue

            cnt += 1
            bfs(i)

        return cnt

            

        
        

        