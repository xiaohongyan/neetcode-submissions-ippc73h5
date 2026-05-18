class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        resIdx = [0,0] # start index, end index(inclusive)
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i + 1][j -1]:
                        dp[i][j] = True 
                
                        if j - i > resIdx[1] - resIdx[0]:
                            resIdx = [i, j]
        
        return s[resIdx[0] : resIdx[1] + 1]


        