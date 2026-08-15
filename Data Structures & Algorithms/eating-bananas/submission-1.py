class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        output = float('inf')
        l, r = 1, max_pile
        while l <= r:
            total_time = 0
            m = (l + r) // 2
            for pile in piles:
                total_time += -(-pile // m)
            if total_time <= h:
                output = min(output, m)
                r = m - 1
            else:
                l = m + 1
        return output