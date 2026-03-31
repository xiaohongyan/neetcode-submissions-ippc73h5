class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = [] # time to reach target

        for p, s in pair:
            t = (target - p) / s
            if not stack or t > stack[-1]: # current car can't form a fleet with the previous one
                stack.append(t)
        
        return len(stack)
                


        