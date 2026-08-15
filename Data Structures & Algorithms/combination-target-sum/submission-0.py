class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def traverse(curr_idx, curr_sum, curr_com):
            if curr_sum < target and curr_idx < len(nums):
                traverse(curr_idx, (curr_sum + nums[curr_idx]), curr_com + [nums[curr_idx]])
                traverse(curr_idx + 1, curr_sum, curr_com)
            else:
                if curr_sum == target:
                    res.append(curr_com[:])
                return
        traverse(0, 0, [])
        return res