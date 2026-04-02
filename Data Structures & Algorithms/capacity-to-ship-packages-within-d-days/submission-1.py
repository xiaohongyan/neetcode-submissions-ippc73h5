class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)

        l = max(weights) # minimum capacity
        r = sum(weights)
        res = r

        while l <= r:
            capacity  = (r + l) // 2
            total_day = 1
            weight  = 0

            # calculate the total day
            for w in weights:
                if weight + w <= capacity :
                    weight += w
                else:
                    total_day += 1 
                    if total_day > days:
                        break
                    weight  = w  # calculate weight from w
            
            if total_day <= days:
                res = capacity
                r = capacity - 1
            else:
                l = capacity + 1
        return res
            


        