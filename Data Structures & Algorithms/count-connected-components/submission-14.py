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

        def dfs(i):
            for neighbor in adj[i]:
                if visited[neighbor]:
                    continue
                visited[neighbor] = True    
                dfs(neighbor)

        for i in range(n):
            if visited[i]:
                continue
            cnt += 1
            visited[i] = True
            dfs(i)

        return cnt
