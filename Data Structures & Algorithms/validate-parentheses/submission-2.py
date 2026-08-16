class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        braces = {"]": "[", "}": "{", ")": "("} # opeing: closing
        opening_braces = "[{("
        braces_stack = []
        for brace in s:
            if brace in opening_braces:
                braces_stack.append(brace)
                continue
            if not braces_stack or braces[brace] != braces_stack[-1]:
                return False
            braces_stack.pop()
        if braces_stack:
            return False
        return True
