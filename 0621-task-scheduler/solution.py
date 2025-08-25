class Solution:
    #Each CPU interval can be idle or allow the completion of one task
    #there has to be a gap of at least n intervals between two tasks with the same label
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1
        heap = []
        for task, count in counter.items():
            heap.append(-count)
        heapq.heapify(heap)
        queue = deque()
        curr = 0
        while queue or heap:
            # print(curr)
            # print(queue)
            # print(heap)
            while queue and queue[0][0] <= curr:
                time, count = queue.popleft()
                heapq.heappush(heap, count)
            if heap:
                count = heapq.heappop(heap) + 1
                if count != 0:
                    queue.append([curr + n + 1, count])
            curr += 1
        
        return curr
