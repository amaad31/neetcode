class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target <= 0 or not candidates:
            return [] 

        candidates.sort()
        nums = candidates
        res = []
        def dfs(i, cur_sum, cur_res):
            if cur_sum == target:
                res.append(cur_res[:])
                return
            
            if cur_sum > target or i == len(nums):
                return
            
            cur_res.append(nums[i])
            dfs(i + 1, cur_sum + nums[i], cur_res)
            cur_res.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, cur_sum, cur_res)
        
        dfs(0, 0, [])
        return res
         