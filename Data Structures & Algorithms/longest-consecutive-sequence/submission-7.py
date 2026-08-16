class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seq_map = defaultdict(int)
        nums_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 in nums_set:
                continue
            tmp_num = num + 1
            cur_seq = 1
            while(tmp_num in nums_set):
                cur_seq += 1
                tmp_num += 1
            
            res = max(res, cur_seq)
        return res
