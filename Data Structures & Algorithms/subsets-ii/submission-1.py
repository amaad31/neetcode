class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        nums.sort()

        def dfs(i, cur_res):
            if i == len(nums):
                res.append(cur_res[:])
                return

            cur_res.append(nums[i])
            dfs(i + 1, cur_res)
            cur_res.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur_res)
        
        dfs(0, [])
        return res