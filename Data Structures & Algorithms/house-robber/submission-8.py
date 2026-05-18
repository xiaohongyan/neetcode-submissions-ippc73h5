class Solution:
    def rob(self, nums: List[int]) -> int:
            
        n1 = 0
        n2 = 0

        for i in range(len(nums)):
            tmp = n2
            n2 = max(n2, n1 + nums[i])
            n1 = tmp

        return n2
