class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        n1 = nums[0]
        n2 = max(nums[0], nums[1])

        for i in range(2, n):
            tmp = n2
            n2 = max(n2, n1 + nums[i])
            n1 = tmp

        return n2
