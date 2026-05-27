class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n1 = len(text1)
        n2 = len(text2)

        if n1 > n2:
            n1, n2 = n2, n1
            text1, text2 = text2, text1

        dp = [0] * (n1 + 1)
        
        for i in range(n2 - 1, -1, -1):
            diag = dp[n1]

            for j in range(n1 - 1, -1, -1):
                tmp = dp[j]

                if text1[j] == text2[i]:
                    dp[j] = 1 + diag
                else:
                    dp[j] = max(dp[j], diag, dp[j + 1])

                diag = tmp
        
        return dp[0]