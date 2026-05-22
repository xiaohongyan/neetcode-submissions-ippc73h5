class Solution:
    """
   1. 核心数学转换：化“相撞”为“加减”
    我们用一个具体的例子来看看两两相撞的本质是什么。
    假设你有 4 块石头：[a, b, c, d]。
        1. 让 a 和 b 相撞，假设 a > b，剩下的重量是 a - b。
	2. 接下来让这个结果 (a - b) 和 c 相撞，假设 c > (a - b)，剩下的重量是 c - (a - b) = c - a + b。
	3. 最后让这个结果和 d 相撞，假设 d > (c - a + b)，剩下的重量是 d - (c - a + b) = d - c + a - b。
    把最后的式子整理一下：a + d - (b + c)。
    惊人的结论出现了： 无论你用什么顺序、两两怎么相撞，最后剩下来的石头重量，本质上就是把这堆石头分成了两组（一组前面带 + 号，一组前面带 - 号），
    然后求这两组重量差的绝对值。
	• 带 + 号的一组总重量设为 $P$。
	• 带 - 号的一组总重量设为 $N$。
	• 我们要求的就是：让 $|P - N|$ 尽可能的小。
    2. 降维打击：怎么变成 0-1 背包？
    既然我们要让两堆石头的差值 $|P - N|$ 尽可能小，那就意味着这两堆石头的重量要尽可能接近总重量的一半（total // 2）。
    这不就变成了：
	有一个容量为 target = total // 2 的背包，我们要从一堆石头里挑一些放进去，求这个背包最多能装多重的石头？
	• 背包容量：target = total // 2
	• 物品重量：石头的重量 stone
	• 物品价值：石头的重量 stone（因为能装多重就装多重，求最大重量）
     只要你的背包塞得越满（越接近 total // 2），剩下没放进背包的另一堆石头和它的差距就越小。
    """
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        capacity = total // 2 

        n = len(stones)

        # dp[j] 表示容量为 j 的背包最多能装多重的石头
        dp = [0] * (capacity + 1)
        dp[0] = 0

        for s in stones:
            for i in range(capacity, s - 1, -1):
                dp[i] = max(dp[i], dp[i - s] + s)

        # dp[target] 是其中一堆石头的最大重量 P
        # 那么另一堆石头的重量 N 就是 total - dp[target]
        # 最终的最小差值就是两者的绝对值差：(total - dp[target]) - dp[target]
        return total - dp[capacity] * 2 