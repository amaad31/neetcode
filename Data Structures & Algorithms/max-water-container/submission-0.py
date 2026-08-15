class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0
        while l < r:
            curr_vol = min(heights[l], heights[r]) * (r - l)
            max_vol = max(max_vol, curr_vol)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_vol