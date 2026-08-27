class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def calH(k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours
        while l < r:
            mid = l + (r - l) // 2
            if calH(mid) <= h:
                r = mid
            else:
                l = mid + 1
        return l