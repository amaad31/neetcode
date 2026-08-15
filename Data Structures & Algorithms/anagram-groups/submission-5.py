from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for cur_str in strs:
            cur_counter_map = dict(sorted(Counter(cur_str).items()))
            str_code = ""
            for ch, count in cur_counter_map.items():
                str_code += str(count) + ch
            
            res[str_code].append(cur_str)
        
        return list(res.values())
