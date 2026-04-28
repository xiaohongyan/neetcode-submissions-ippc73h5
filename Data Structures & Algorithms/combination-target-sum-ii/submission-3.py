class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subSet = []
        candidates.sort()

        def backtracking(i, remains):

            if remains == 0:
                res.append(subSet.copy()) 
                return
            
            for j in range(i, len(candidates)):

                if candidates[j] > remains:
                    break

                # remove duplicate
                if j > i and candidates[j-1] == candidates[j]:
                    continue

                # include candidates[i]
                subSet.append(candidates[j])
                backtracking(j + 1, remains - candidates[j])
                
                # not include candidates[i]
                subSet.pop()


        backtracking(0, target) 
        return res