class Solution:
    def isValidChar(self, ch: str) -> bool:
        if not ch.isalpha() and not ch.isdigit():
            return False
        return True

    def isPalindrome(self, s: str) -> bool:
        if not s:
            False
        s = s.replace(" ","").lower()
        l, r = 0, len(s) - 1
        while l <= r:
            left_ch = s[l]
            right_ch = s[r]
            if not self.isValidChar(left_ch):
                l += 1
                continue
            if not self.isValidChar(right_ch):
                r -= 1
                continue
            if left_ch != right_ch:
                return False
            l += 1
            r -= 1
        return True