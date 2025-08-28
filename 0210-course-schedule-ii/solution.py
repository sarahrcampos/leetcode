class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b) #a depende de b
        res = []
        
        visited = {}
        def dfs(node):
            if node in visited and visited[node] == 1: #msm path -> ciclo
                return False
            if node in visited and visited[node] == 2:
                return True
            if not graph[node]:
                visited[node] = 2
                res.append(node)
                return True
            
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            res.append(node)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        
        return res
