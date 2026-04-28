class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        subSet = []
        nums.sort()

        def backtracking(i):

            if i >= len(nums):
                res.append(subSet.copy())
                #res.append(subSet) subSet is only reference, not actual list, 
                # at the end, it will be empty
                return 

            # include nums[i]
            subSet.append(nums[i])
            backtracking(i + 1)

            # not include nums[i]
            subSet.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtracking(i + 1)

        backtracking(0)
        return res