class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        res = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        cur_sum = 0

        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum - k in prefix_map:
                res += prefix_map[cur_sum - k] 
            prefix_map[cur_sum] += 1

        return res