class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        res = []
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def dfs(i, cur_res):
            if i == len(s):
                res.append(cur_res[:])
                return

            for j in range(i, len(s)):
                if isPalindrome(s, i ,j):
                    cur_res.append(s[i:j + 1])
                    dfs(j + 1, cur_res)
                    cur_res.pop()
                
        dfs(0, [])
        return res
            
        

