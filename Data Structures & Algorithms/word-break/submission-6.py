class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not wordDict:
            return False

        wordSet = set(wordDict)
        
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] means whether the substring s[i:] can be segmented
        dp[n] = True

        for i in range(n -1, -1, -1):
            for w in wordDict:
                if i + len(w) - 1 < n and  s[i : i + len(w)] in wordDict:
                    dp[i] = dp[i + len(w)]
                
                if dp[i]:
                    break

        return dp[0]