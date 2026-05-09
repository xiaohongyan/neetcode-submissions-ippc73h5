class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(node):
            if node == n:
                return

            for i in range(n):
                if isConnected[node][i] != 1 or visited[i]:
                        continue
                visited[i] = True
                dfs(i)

        provinces = 0
        for node in range(n):
            if not visited[node]:

                dfs(node)
                visited[node] = True
                provinces += 1

        return provinces    