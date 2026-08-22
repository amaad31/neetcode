class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if 0 >= k  or 0 >= n:
            return []
        
        res = []
        def dfs(i, cur_res):
            if len(cur_res) == k:
                res.append(cur_res[:])
                return
            
            if i == (n + 1):
                return
            
            cur_res.append(i)
            dfs(i + 1, cur_res)
            cur_res.pop()
            dfs(i + 1, cur_res)

        dfs(1, [])
        return res