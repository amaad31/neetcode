class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        leng = len(nums)

        def dfs(i, cur_res):
            if i == leng:
                res.append(cur_res[:]) # copies cur_sol in res
                return
            
            cur_res.append(nums[i])
            dfs(i + 1, cur_res)
            cur_res.pop()
            dfs(i + 1, cur_res)
            
        dfs(0, [])
        return res