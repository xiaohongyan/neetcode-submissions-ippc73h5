class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not wordDict:
            return False
            
        wordSet = set(wordDict)
        
        n = len(s)

        # dp[i] = 1 means whether the substring s[i:] can be segmented
        # dp[i] = -1 unvisited
        # dp[i] = 0 means whether the substring s[i:] can NOT be segmented
        dp = [None] * (n + 1)  
        dp[n] = True

        def dfs(i):

            if i == n:
                return True

            if dp[i] != None:
                return dp[i]

            for j in range(i, n):
                if s[i : j + 1] in wordSet and dfs(j + 1):
                    dp[i] = True
                    return True

            dp[i] = False
            return False

        return dfs(0)