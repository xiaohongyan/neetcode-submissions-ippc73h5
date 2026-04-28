class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subSet = []
        nums.sort()

        def backtracking(i, remains):

            if remains == 0:
                res.append(subSet.copy()) 
                return
            
            for j in range(i, len(nums)):

                if nums[j] > remains:
                    return

                # include nums[i]
                subSet.append(nums[j])
                backtracking(j, remains - nums[j])
                
                # not include nums[i]
                subSet.pop()
                # dont need the following line since j will be ++ in the for loop
                # backtracking(j + 1, remains)

        backtracking(0, target) 
        return res