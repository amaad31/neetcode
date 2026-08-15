class Solution:
    def climbStairs(self, n: int) -> int:
        self.res = 0
        def dfs(num: int):
            if num == 0:
                self.res += 1
            elif num < 0:
                return
            dfs(num - 1)
            dfs(num - 2)
        dfs(n)
        return self.res
            