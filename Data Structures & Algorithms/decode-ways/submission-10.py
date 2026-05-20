class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or int(s[0]) == 0:
            return 0

        n =len(s)
        prev = 1
        prev_prev = 1 
        res = 0
        for i in range(1, n):
            cur = 0
            one_digit = int(s[i])

            # 1 digit
            if 1 <= one_digit <= 9:
                cur += prev

            # 2 digit
            two_digit = int(s[i-1 : i + 1])
            if 10 <= two_digit  <= 26:
                cur += prev_prev
            
            prev_prev = prev
            prev = cur

        return prev