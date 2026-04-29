class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        count = [n, n] # [0]- number of ( left,  [1]- number of )
        par = ['(',')']
        res = []
        cur = []

        def backtracking():
            if len(cur) == 2 * n:
                res.append("".join(cur.copy()))
                return

            for i in range(len(par)):
                if count[i] < 1:
                    continue

                if i ==  1 and count[0] >= count[1]:
                    continue
                
                cur.append(par[i])
                count[i] -= 1
                backtracking()

                cur.pop()
                count[i] += 1
        
        backtracking()
        return res
        



        