class Solution:
    def numSquares(self, n: int) -> int:

        squares = [i * i for i in range(1, int(n ** 0.5) + 1)] # sorted

        squares.sort(reverse = True)
        m = len(squares)
        memo = {}
        
        def dfs(remain):

            if remain == 0:
                return 0

            if remain in memo:
                return memo[remain]

            res = n + 1
            for s in squares:
                if s > remain:
                    continue
                
                res = min(res, dfs(remain - s) + 1)

            memo[remain] = res
            return res
    
        return dfs(n)