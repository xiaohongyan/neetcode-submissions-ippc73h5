class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not wordDict:
            return False

        n = len(s)
        dp = [False] * (n + 1)  # dp[i] means whether the substring s[i:] can be segmented
        dp[n] = True

        for i in range(n -1, -1, -1):
            for j in range(i, n):
                if dp[j + 1] and s[i : j + 1] in wordDict:
                    dp[i] = True

        return dp[0]




        