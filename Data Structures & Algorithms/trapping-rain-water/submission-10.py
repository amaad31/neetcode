class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        maxL, maxR = 0, 0
        l, r = 0, len(height) - 1
        while l < r:
            maxL, maxR = max(maxL, height[l]), max(maxR, height[r])
            res += (maxL - height[l]) + (maxR - height[r])
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res