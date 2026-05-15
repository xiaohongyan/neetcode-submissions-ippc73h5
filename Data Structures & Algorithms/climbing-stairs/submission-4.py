class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        one, two = 1, 1
        
        for i in range(2, n + 1):
            res = one + two
            one = two
            two = res
            
        return res