class Solution:
    
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1 = len(word1)
        n2 = len(word2)

        if n1 > n2:
            n1, n2 = n2, n1
            word1, word2 = word2, word1

        dp = [n2] * (n1 + 1)
        next_dp = [n2] * (n1 + 1)

        # initialize for when word2 is empty
        for i in range(n1 + 1): 
            dp[i]= n1 - i
          
        for i in range(n2 - 1, -1, -1):
            diagnol = dp[n1]

            # 更新当前行的右边界：当 word1 为空，word2 剩下 n2 - i 长度时的插入步数
            dp[n1]= n2 - i

            for j in range(n1 - 1, -1, -1): 
                tmp = dp[j] # 暂存当前未被覆盖的旧值（它会成为下一个左边格子的右下角）

                if word1[j] == word2[i]:
                    dp[j] = diagnol
                else:
                    # 字符不同，1 + min(下方, 右方, 右下方)
                    # dp[j] 是下方（旧的 dp[j]）
                    # dp[j+1] 是右方（刚刚在上一轮内循环更新掉的 dp[j+1]）
                    # diagnol 是右下方
                    dp[j] = 1 + min(diagnol, dp[j + 1], dp[j])

                diagnol = tmp
                   
        return dp[0]