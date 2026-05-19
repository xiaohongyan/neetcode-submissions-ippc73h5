class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        dp =[[False] * n for _ in range(n)]

        res = 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i +1][j -1]:
                        dp[i][j] = True
                    
                if dp[i][j]:
                    res += 1
        
        return res


        