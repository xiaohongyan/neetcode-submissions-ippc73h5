class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        resIdx = [0, 0] # start index, end index(inclusive)

        def expend(left, right):
            nonlocal resIdx
            while left >= 0 and right < n and s[left] == s[right]:       
                if right - left > resIdx[1] - resIdx[0]:
                    resIdx = [left, right]
                
                left -= 1
                right += 1


        for i in range(n):

            # odd length string
            expend(i,i)

            # even length string
            expend(i,i + 1)

        return s[resIdx[0] : resIdx[1] + 1]