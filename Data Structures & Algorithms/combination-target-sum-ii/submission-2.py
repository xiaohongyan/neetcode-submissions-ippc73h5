class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []
        candidates.sort()

        def backtracking(i, remains):

            if remains == 0:
                res.append(subSet.copy()) 
                return
            
            if i >= len(candidates) or candidates[i] > remains:
                return

            # include candidates[i]
            subSet.append(candidates[i])
            backtracking(i + 1, remains - candidates[i])
            
            # not include candidates[i]
            subSet.pop()
            # remove duplicate
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            backtracking(i + 1, remains)

        backtracking(0, target) 
        return res