class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        nums = heights
        max_area = 0
        len_nums = len(nums)
        l, r = 0, len_nums - 1

        while l < r:
            left_bar = nums[l]
            right_bar = nums[r]
            cur_area = min(right_bar, left_bar) * (r  - l)
            max_area = max(max_area, cur_area)

            if right_bar < left_bar:
                r -= 1
            else:
                l += 1

        return max_area