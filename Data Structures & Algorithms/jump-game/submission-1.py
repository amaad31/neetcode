class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.res = False
        def dfs(idx):
            if idx >= (len(nums) - 1):
                self.res = True
                return
            if nums[idx] == 0:
                return
            for jump in range(nums[idx], 0, -1):
                dfs(idx + jump)
        dfs(0)
        return self.res
            