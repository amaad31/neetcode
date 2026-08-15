class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        res = 0
        cur_res = 0
        for num in nums:
            cur_res = cur_res + num
            if cur_res < 0:
                cur_res = 0
            res = max(res, cur_res)
        return res
