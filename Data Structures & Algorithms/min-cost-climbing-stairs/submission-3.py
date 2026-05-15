class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        pay = [0] * n

        pay[0], pay[1] = cost[0], cost[1]

        for i in range (2, n):
            pay[i] = min(pay[i - 2], pay[i - 1]) + cost[i]
        
        return min(pay[n -1], pay[n -2])

        