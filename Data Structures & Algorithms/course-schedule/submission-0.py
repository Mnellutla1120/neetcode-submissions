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
                #We alr took this course, we cannot take it again
                return False
            if preMap[course] == []:
                 return True #we can take the course

            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False #if we don't have the prerequisite necessary for our course in question
            visited.remove(course) #cannot take the course
            preMap[course] = [] #maps prereq to course
            return True
        for c in range(numCourses):
             if not dfs(c):
                 return False
        return True
            




