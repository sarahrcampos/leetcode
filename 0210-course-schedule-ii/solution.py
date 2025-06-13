class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependsOf = defaultdict(list)
        for a, b in prerequisites:
            dependsOf[a].append(b)
        
        visited = set()
        visiting = set()
        res = []
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            if course not in dependsOf:
                visited.add(course)
                res.append(course)
                return True
            
            
            visiting.add(course)
            for courseB in dependsOf[course]:
                if not dfs(courseB):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if i in visited: continue
            if not dfs(i):
                return []
        
        return res

