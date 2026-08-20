class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        nums_counter = Counter(nums)
        record_map = defaultdict(int)
        res = []
        def dfs(cur_res):
            if len(cur_res) == len(nums):
                res.append(cur_res[:])
                return
            
            for i, num in enumerate(nums):
                record_map[num] += 1
                if record_map[num] > nums_counter[num] or (i > 0 and num == nums[i - 1]):
                    record_map[num] -= 1
                    continue
                cur_res.append(num)
                dfs(cur_res)
                cur_res.pop()
                record_map[num] -= 1
        dfs([])
        return res

