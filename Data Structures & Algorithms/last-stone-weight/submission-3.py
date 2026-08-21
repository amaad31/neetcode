class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        max_heap = stones

        while len(max_heap) > 1:
            hs1 = heapq.heappop(max_heap)
            hs2 = heapq.heappop(max_heap)
            if hs1 < hs2:
                heapq.heappush(max_heap, hs1 - hs2)
            elif hs1 > hs2:
                heapq.heappush(max_heap, hs2 - hs1)
        
        if not max_heap:
            return 0
        
        return -max_heap[0]

