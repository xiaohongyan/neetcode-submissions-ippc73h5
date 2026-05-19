class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        resIdx = [0,0] # start index, end index(inclusive)

        for i in range(n):

            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:       
                if right - left > resIdx[1] - resIdx[0]:
                    resIdx = [left, right]
                
                left -= 1
                right += 1
            
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:       
                if right - left > resIdx[1] - resIdx[0]:
                    resIdx = [left, right]
                
                left -= 1
                right += 1

        return s[resIdx[0] : resIdx[1] + 1]