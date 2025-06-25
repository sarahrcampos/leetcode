class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        answer = []
        for u, v in queries:
            queue = deque([u])
            visited = set()
            result = False
            while queue:
                node = queue.popleft()
                if node == v:
                    result = True
                    break
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            answer.append(result)
        return answer

            

