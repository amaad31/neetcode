class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        l, r = 0, 0
        res = 0
        chrs_record = defaultdict(int)
        while r < len(s):
            chrs_record[s[r]] += 1
            while(r - l + 1 - max(chrs_record.values())) > k:
                chrs_record[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res 