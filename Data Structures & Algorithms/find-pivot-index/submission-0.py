class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        cur_sum = 0
        for i, num in enumerate(nums):
            if (2*cur_sum) == (total_sum - num):
                return i
            cur_sum += num
        return -1