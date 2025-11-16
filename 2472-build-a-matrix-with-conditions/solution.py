class Solution:
    def buildGraph(self, edges):
        #a is before b, so b depends of a ==> b -> a
        graph = {}
        for a, b in edges:
            if b not in graph:
                graph[b] = []
            graph[b].append(a)
        return graph

    def topologicalsort(self, graph, k):
        visited = {} #not in visited = ok, visited == 1 -> cycle, visited == 2 -> visited in different path
        sort = []
        def dfs(node):
            if node in visited and visited[node] == 1:
                return False
            if node in visited and visited[node] == 2:
                return True
            
            visited[node] = 1
            if node in graph:
                for neighbor in graph[node]:
                    if not dfs(neighbor):
                        return False
            visited[node] = 2
            sort.append(node)
            return True
        
        for i in range(1, k+1):
            if not dfs(i):
                return []
        return sort


    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        #topological sort na matriz
        rows = self.buildGraph(rowConditions)
        cols = self.buildGraph(colConditions)
        result = [[0] * k for _ in range(k)]

      #  print(rows)
      #  print(cols)
        rowLocation = {}
        rowSort = self.topologicalsort(rows, k)
      #  print(rowSort)
        if not rowSort:
            return []
        for i, n in enumerate(rowSort):
            rowLocation[n] = i

        colSort = self.topologicalsort(cols, k)
       # print(colSort)
        if not colSort:
            return []
        for j, n in enumerate(colSort):
            result[rowLocation[n]][j] = n
        
        return result


