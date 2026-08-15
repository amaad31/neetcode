from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_map_s = Counter(s)
        counter_map_t = Counter(t)
        if len(counter_map_s) != len(counter_map_t):
            return False

        for ch, count in counter_map_s.items():
            if counter_map_t[ch] != count:
                return False
        
        return True


    