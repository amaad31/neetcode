class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        len_idx_list = 0
        min_num = 0
        if min(nums) < 0:
            min_num = min(nums)
            len_idx_list = abs(min(nums)) + max(nums) + 1
        else:
            min_num = 0
            len_idx_list = max(nums) + 1
        idx_list = [0] * len_idx_list
        for num in nums:
            idx_list[num - (min_num)] = 1
        cur_result = 0
        result = 0
        for bit in idx_list:
            if bit:
                cur_result += 1
                result = max(result, cur_result)
            else:
                cur_result = 0
        return result