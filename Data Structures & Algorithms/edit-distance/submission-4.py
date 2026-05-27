class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1 = len(word1)
        n2 = len(word2)

        dp = [[n1 + n2] * (n2 + 1) for _ in range(n1 + 1) ]
        # dp[i][j] means the number of operation such that substring 0-i of word1 are the same as substring 0-j of word2

        for i in range(n1 + 1):
            dp[i][0] = i

        for i in range(n2 + 1):
            dp[0][i] = i

        for i in range(n1):
            for j in range(n2):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    # dp[i][j - 1]: remove word2[j]
                    # dp[i - 1][j]: add word2[j] at word1[i]
                    # dp[i][j]: replace word1[i] with word2[j]
                    dp[i + 1][j + 1] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i][j])
                    
        return dp[n1][n2]