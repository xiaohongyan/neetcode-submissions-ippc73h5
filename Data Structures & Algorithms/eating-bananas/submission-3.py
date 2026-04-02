class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles)
        r = piles[n-1] # max rate
        l = 1
        min_rate = r
        while l <= r:
            mid = (r + l) //2 
            total_hour = 0
            for p in piles:
                total_hour += math.ceil(p / mid) 
            if total_hour > h:
                l = mid + 1
            else:
                min_rate = min(min_rate, mid)
                r = mid - 1
        return min_rate

            

        