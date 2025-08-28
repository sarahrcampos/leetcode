#prerequisites[i] = [a,b] => a depende de b
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = {}
        def dfs(node):
            if node in visited and visited[node] == 1: #visitado no mesmo path -> ciclo
                return False
            if node in visited and visited[node] == 2:
                return True
            if node not in graph:
                return True
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True
