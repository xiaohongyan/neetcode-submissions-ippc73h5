class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        cycle = set()
        def dfs(course):

            if course in cycle:
                return False
            if preMap[course] == []:
                return True

            cycle.add(course)
            for p in preMap[course]:
                if not dfs(p):
                    return False

            cycle.remove(course)
            preMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True
            



        

        

        