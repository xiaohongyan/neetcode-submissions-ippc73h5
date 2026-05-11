class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        visited = [False] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        cycle = set()
        cycle_start = -1

        for e in edges:
            p, v = e[0], e[1]
            adj[p].append(v)
            adj[v].append(p)

        def dfs(node, parent):
            nonlocal cycle_start

            if visited[node]:
                cycle_start = node
                return True

            visited[node] = True
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                if dfs(neighbor, node):
                    if cycle_start != -1:
                        cycle.add(node)
                    if node == cycle_start:  
                        cycle_start = -1
                    return True
            
            return False


        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []