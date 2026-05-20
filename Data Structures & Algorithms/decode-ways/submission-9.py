class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or int(s[0]) == 0:
            return 0

        n =len(s)
        prev_1 = 1
        prev_2 = 1 
        res = 0
        for i in range(1, n):
            res = 0
            one_digit = int(s[i])

            # 1 digit
            if 1 <= one_digit <= 9:
                res += prev_1

            # 2 digit
            two_digit = int(s[i-1 : i + 1])
            if 10 <= two_digit  <= 26:
                res += prev_2
            
            prev_2 = prev_1
            prev_1 = res

        return prev_1