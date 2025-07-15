class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1
        heap = []
        for task, count in counter.items():
            heapq.heappush(heap, [-count, task, 0])

        time = 0
        queue = deque()
        while heap or queue:
            while queue and queue[0][2] <= time:
                heapq.heappush(heap, queue.popleft())
            if heap:
                count, task, curTime = heapq.heappop(heap)
                if count + 1 < 0:
                    queue.append([count+1, task, time + n + 1])
            time += 1

        return time



