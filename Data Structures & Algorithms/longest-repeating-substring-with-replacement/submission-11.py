class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        char_map = defaultdict(int)
        max_window = 0
        tracking_k = k
        ch_max = 0
        while r < len(s):
            char_map[s[r]] += 1
            ch_max = max(char_map[s[r]], ch_max)
            while ((r - l + 1) - ch_max) > k:
                char_map[s[l]] -= 1
                if char_map[s[l]] < 1:
                    del char_map[s[l]]
                l += 1
            max_window = max(max_window, (r - l + 1))
            r += 1
        return max_window