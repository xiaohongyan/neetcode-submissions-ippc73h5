class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(node):
            dq = deque()
            dq.append(node)
             
            while dq:
                cur = dq.popleft()
                for neighbor in range(n):
                    if isConnected[cur][neighbor] != 1 or visited[neighbor]:
                        continue

                    dq.append(neighbor)
                    visited[neighbor] = True

        provinces = 0
        for node in range(n):
            if not visited[node]:

                bfs(node)
                visited[node] = True
                provinces += 1

        return provinces
        