class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def backtracking(i):
            if i == len(nums):
                res.append(nums.copy())
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtracking(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        backtracking(0)
        return res

        