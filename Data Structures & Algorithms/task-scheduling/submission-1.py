class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        heap = [-task for task in list(Counter(tasks).values())]
        heapq.heapify(heap)

        res = 0
        queue = deque()

        while heap or queue:
            while queue and queue[0][1] <= res:
                heapq.heappush(heap, queue.pop()[0])
            if heap:
                cur_task = heapq.heappop(heap)
                cur_task += 1
                if cur_task != 0:
                    queue.append((cur_task, res + n + 1))
            
            res += 1
        
        return res

