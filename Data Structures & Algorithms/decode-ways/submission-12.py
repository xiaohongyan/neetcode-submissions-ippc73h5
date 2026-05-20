class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or int(s[0]) == 0:
            return 0

        n = len(s)
        dp = [-1] * n

        def dfs(i):

            if dp[i]  != -1:
                return dp[i]

            if i == 0:
                return 1
            
            cur = 0
            # one digit
            if 1 <=int(s[i]) <= 9:
                cur += dfs(i - 1)

            # two digit
            two_digit = int(s[i-1: i + 1])
            if 10 <= two_digit<= 26:
                cur += dfs(i - 2) if i-2 >= 0 else 1
            
            dp[i] = cur
            return dp[i]
        
        return dfs(n-1)