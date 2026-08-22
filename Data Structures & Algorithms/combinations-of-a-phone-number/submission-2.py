class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }        
        res = []
        def dfs(i: int, cur_res: str) -> None:
            if i == len(digits):
                res.append(cur_res)
                return
            
            for ch in digitToChar[digits[i]]:
                cur_res += ch
                dfs(i + 1, cur_res)
                cur_res = cur_res[:-1]
            
        dfs(0, "")
        return res
