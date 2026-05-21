class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if not coins:
            return 0 if amount == 0 else -1
        
        if amount == 0:
            return 0
        
        coins.sort()
        dq = deque()
        dq.append(amount)
        seen = [False] * (amount + 1)
        cnt = 0

        while dq:
            cnt += 1
            for _ in range(len(dq)):
                cur = dq.popleft()
                
                for c in coins:
                    remain = cur - c
                    if remain == 0:
                        return cnt
                    if remain < 0:
                        break
                    if seen[remain]:
                        continue

                    dq.append(remain)
                    seen[remain] =  True

        return -1
                
                


