class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adj = { i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            indegree[course] += 1   
            adj[pre].append(course)

        dq = deque()
        for c in range(numCourses):
            if  indegree[c] == 0:
                dq.append(c)

        while dq:
            cur = dq.popleft()
            res.append(cur)
            for c in adj[cur]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    dq.append(c)
            
        return res if len(res) == numCourses else []

"""
面试官可能会追问：“如果存在多个合法的修课顺序，你的代码能处理吗？”

你的回答：是的，Kahn 算法可以处理。在同一时刻，如果有多个课程的入度都变为 0，它们都会被加入 deque。由于 deque 的 FIFO（先进先出）特性，我们会按照它们入队的顺序处理。如果想要特定的顺序（比如按课程编号排序），可以将 deque 换成 heapq (最小堆)。
"""