class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        idx_map = {}
        res = 0
        l = 0
        for r, ch in enumerate(s):
            if ch in idx_map:
                while s[l] != ch:
                    del idx_map[s[l]]
                    l += 1
                l += 1
            idx_map[ch] = r
            res = max(res, r - l + 1)
        return res