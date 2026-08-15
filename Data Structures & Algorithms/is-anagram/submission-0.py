class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        
        for s_char in s:
            hash_s[s_char] = hash_s.get(s_char, 0) + 1

        for t_char in t:
            hash_t[t_char] = hash_t.get(t_char, 0) + 1
        
        return (True if hash_t == hash_s else False)