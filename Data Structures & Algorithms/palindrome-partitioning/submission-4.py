class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        n = len(s)
        checked = {}

        def isPalidrome(curStr):
            if curStr in checked: 
                return checked[curStr]
            
            l = 0
            r = len(curStr) - 1
            while l < r:
                if curStr[l] != curStr[r]:
                    checked[curStr] = False
                    return False
                l += 1
                r -= 1

            checked[curStr] = True
            return True


        def backtracking(i):

            if i >= len(s):
                res.append(cur.copy())
                return 
            
            for j in range(i, n):
                curS = s[i : j +1]
                if not isPalidrome(curS):
                    continue
                
                cur.append(curS)
                backtracking(j + 1)
                cur.pop()

        backtracking(0)
        return res


            


        