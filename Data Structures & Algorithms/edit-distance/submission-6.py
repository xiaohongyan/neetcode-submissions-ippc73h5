class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1 = len(word1)
        n2 = len(word2)

        memo = {}
        # dp[i][j] means the number of operation such that  word1[i:] are the same as word2[j:]

        def dfs(i, j):
            if i >= n1:
                return n2 -j
            if j >= n2:
                return n1 - i

            if (i, j) in memo:
                return memo[(i, j)]

            res = 0
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

            return memo[(i, j)]
                    
        return dfs(0, 0)