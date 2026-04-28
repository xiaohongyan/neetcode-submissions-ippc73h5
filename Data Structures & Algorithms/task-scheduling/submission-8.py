class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord('A')] += 1

        max_freq = max(count)
        maxCount = 0 # number of the task with max_freq
        for c in count:
            maxCount += 1 if c == max_freq else 0

        time = (max_freq - 1) * (n + 1) + maxCount
        return max(time, len(tasks))