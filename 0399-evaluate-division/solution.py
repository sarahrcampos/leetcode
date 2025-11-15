#equations -> [a, b] (variáveis)
#values -> a/b = value
#queries-> [c, d]
#precisa descobrir c/d = ?
#retornar a resposta pra cada query, se não der pra determinar retornar -1
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:        
        graph = {}
        for i in range(len(equations)):
            a, b = equations[i]
            result = values[i]
            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()
            graph[a].add((b, result))
            graph[b].add((a, 1/result))
            graph[a].add((a, 1))
            graph[b].add((b, 1))
        print(graph)        
        
        cache = {}
        visited = set()
        def dfs(curr, end):
            if curr not in graph or end not in graph:
                return -1
            if curr == end:
                return 1            
            if (curr, end) in cache:
                return cache[(curr, end)]            

            visited.add(curr)
            for neighbor, value in graph[curr]:
                if neighbor in visited:
                    continue
                total = dfs(neighbor, end)
                if total != -1:
                    visited.remove(curr)
                    return value * total
            visited.remove(curr)
            return -1


        queryOutput = []
        for i in range(len(queries)):
            qa, qb = queries[i]
            queryOutput.append(dfs(qa, qb))           
        
        return queryOutput
        

