class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        max_area = 0
        len_heights = len(heights)
        l, r = 0, len_heights - 1

        while l < r:
            left_bar = heights[l]
            right_bar = heights[r]
            cur_area = min(right_bar, left_bar) * (r  - l)
            max_area = max(max_area, cur_area)

            if right_bar < left_bar:
                r -= 1
            else:
                l += 1

        return max_area