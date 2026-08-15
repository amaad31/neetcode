class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars_map = defaultdict(int)
        left, right = 0, 0
        res = 0
        while(right < len(s)):
            curr_char = s[right]
            unique_chars_map[curr_char] += 1
            if unique_chars_map[curr_char] > 1:
                while(unique_chars_map[curr_char] > 1):
                    unique_chars_map[s[left]] -= 1
                    left += 1
            res = max(res, (right - left + 1))
            right += 1
        return res

