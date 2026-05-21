class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not wordDict:
            return False
            
        wordSet = set(wordDict)
        
        n = len(s)

        # dp[i] = 1 means whether the substring s[i:] can be segmented
        # dp[i] = -1 unvisited
        # dp[i] = 0 means whether the substring s[i:] can NOT be segmented
        dp = [-1] * (n + 1)  
        dp[n] = True

        def dfs(i):

            if i == n:
                return True

            if dp[i] != -1:
                return True if dp[i] == 1 else False

            for j in range(i, n):
                if dfs(j + 1) and dp[j + 1] and  s[i : j + 1] in wordSet:
                    dp[i] = 1
                    return True

            dp[i] = 0
            return False

        return dfs(0)