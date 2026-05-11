class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            indegree[course] += 1   
            adj[pre].append(course)

        dq = deque()
        
        for c in range(numCourses):
            if  indegree[c] == 0:
                dq.append(c)

        finished = 0
        while dq:
            cur = dq.popleft()
            finished += 1
            for c in adj[cur]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    dq.append(c)
            
        return finished == numCourses



        

        

        