class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or int(s[0]) == 0:
            return 0

        n = len(s)
        dp = [-1] * n

        def dfs(i):

            # Base Case 1: 如果指针成功越过开头（i == -1），说明前面的拆分完全合法，给这条路径记 1 分
            if i < 0:
                return 1
            
            # Base Case 2: 如果来到了第一个字符，它只要不是 '0'（开头已拦截），就只有 1 种解码方式
            if i == 0:
                return 1 if s[0] != '0' else 0

            if dp[i]  != -1:
                return dp[i]
            
            cur = 0
            # one digit
            if 1 <=int(s[i]) <= 9:
                cur += dfs(i - 1)

            # two digit
            two_digit = int(s[i-1: i + 1])
            if 10 <= two_digit<= 26:
                cur += dfs(i - 2) 
            
            dp[i] = cur
            return dp[i]
        
        return dfs(n-1)