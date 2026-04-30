class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        cur = []
        n = len(digits)

        digitMap = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz',
        }

        def backtracking(i):
            if i == n:
                res.append("".join(cur.copy()))
                return

            curStr = digitMap[digits[i]]

            for j in range(len(curStr)):
                cur.append(curStr[j])
                backtracking(i + 1)
                cur.pop()

        
        backtracking(0)
        return res
            


        