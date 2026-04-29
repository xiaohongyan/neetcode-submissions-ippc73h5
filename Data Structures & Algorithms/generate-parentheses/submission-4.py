class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur = []

        def backtracking(left, right):
            if left == right == n:
                res.append("".join(cur.copy()))
                return
                
            if left < n:
                cur.append('(')
                backtracking(left + 1, right)
                cur.pop()

            if left > right:
                cur.append(')')
                backtracking(left, right + 1)
                cur.pop()

        backtracking(0, 0)
        return res
        



        