class Solution:

    # DP
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)

        # dp[i][j] 表示 s[i:j+1] 是否为回文
        dp = [[False] * n for _ in range(n)] # (n - 1) * n
        res = []
        cur = []
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j-1] if j - i >1 else True

        def backtracking(i):
            if i >= len(s):
                res.append(cur.copy())
                return 
            
            for j in range(i, n):  
                if not dp[i][j]:
                    continue
                
                cur.append(s[i : j +1])
                backtracking(j + 1)
                cur.pop()
        
        backtracking(0)
        return res