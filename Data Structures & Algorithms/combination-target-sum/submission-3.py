class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subSet = []
        def backtracking(i, remains):

            if i >= len(nums) or remains <= 0:
                if remains == 0:
                    res.append(subSet.copy()) 
                return

            # include nums[i]
            subSet.append(nums[i])
            backtracking(i, remains - nums[i])
            
            # not include nums[i]
            subSet.pop()
            backtracking(i + 1, remains)

        backtracking(0, target) 
        return res