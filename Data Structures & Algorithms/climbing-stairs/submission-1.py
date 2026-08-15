class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        def dfs(num: int):
            if num == 0:
                return 1
            elif num < 0:
                return 0
            if num in self.memo:
                return self.memo[num]
            self.memo[num] = dfs(num - 1) + dfs(num - 2)
            return self.memo[num]
        return dfs(n)
            