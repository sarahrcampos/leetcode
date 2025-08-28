#times[i] = (ui, vi, wi)
#dijkstra
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append([v,w])

        visited = set()
        minHeap = [[0, k]]
        time = -1
        while minHeap:
            w, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            time = w
            for node2, w2 in graph[node]:
                if node2 not in visited:
                    heapq.heappush(minHeap, [w + w2, node2])
        print(visited)
        return time if len(visited) == n else -1

