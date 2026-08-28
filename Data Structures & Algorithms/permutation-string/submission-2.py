class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s2:
            return False
        target_record = [0] * 26
        for ch in s1:
            target_record[ord(ch) - ord('a')] += 1
        record = [0] * 26
        l, r = 0, 0
        while r < len(s2):
            ch = s2[r]
            record[ord(ch) - ord('a')] += 1
            while (r - l + 1) > len(s1):
                record[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if record == target_record:
                return True
            r += 1
        return False