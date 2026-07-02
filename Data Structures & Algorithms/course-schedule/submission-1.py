class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to the prereqs

        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
             preMap[course].append(pre)

        #store all visited courses along DFS path
        visited = set()

        def dfs(course):
            if course in visited:
                #We are currently taking course, creates DFS cycle
                return False
            if preMap[course] == []:
                 return True #we can take the course since it has no prereqs

            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False #if we don't have the prerequisite necessary for our course in question
            visited.remove(course) #all prereqs resolved, so pop to prevent cycle
            preMap[course] = [] #course has no prereq
            return True
        for c in range(numCourses):
             if not dfs(c):
                 return False
        return True
            




