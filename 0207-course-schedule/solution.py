class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependsOf = defaultdict(list)
        for a, b in prerequisites:
            dependsOf[a].append(b)
        
        visited = set()
        cache = {}
        def dfs(a):
            if a in visited:
                return False
            if a in cache:
                return cache[a]
            if a not in dependsOf:
                return True
            

            res = True
            visited.add(a)
            for b in dependsOf[a]:
                res &= dfs(b)
            visited.remove(a)
            cache[a] = res
            return res
        
        for course in dependsOf:
            if not dfs(course):
                return False
        
        return True

        
        

