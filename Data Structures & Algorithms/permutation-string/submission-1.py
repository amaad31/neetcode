class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        if len(s1) == 0:
            return True
        map_s1 = Counter(s1)
        map_s2 = defaultdict(int)
        for i in range(len(s1)):
            map_s2[s2[i]] += 1
        l, r = 0, len(s1)
        if map_s2 == map_s1:
            return True
        while(r < len(s2)):
            map_s2[s2[r]] += 1
            map_s2[s2[l]] -= 1
            if map_s2[s2[l]] == 0:
                del map_s2[s2[l]]
            if map_s1 == map_s2:
                return True
            l += 1
            r += 1
        return False
