class Solution:
    def rob(self, nums: List[int]) -> int:
#        House:   0   1   2   3   4   5   6   7   8   9   10  11
#        Money:   4  10   3   1   7   2   9   6   5  12    4   8
#                     ✓           ✓       ✓           ✓        ✓

        if not nums:
            return 0

        res = 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        fl, l = nums[0], nums[1]
        for i in range(2, len(nums)):
            res = max(nums[i] + fl, l)
            fl, l = max(fl, l), nums[i] + fl
        
        return res