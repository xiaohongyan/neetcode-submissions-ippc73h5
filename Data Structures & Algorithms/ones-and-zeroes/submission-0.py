class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        # size of largest subset of strs and there are most i 0 and j 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        def getNumberOfOnes(s):
            res = 0
            for c in s:
                if c == '1':
                    res += 1
            return res


        for s in strs:
            ones = getNumberOfOnes(s)
            zeros = len(s) - ones

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]