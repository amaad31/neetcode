class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return False

        res = False
        rows, cols = len(board), len(board[0])
        record = set()
        def dfs(r, c, cur_word):
            nonlocal res
            if cur_word == word:
                res = True
                return
            if cur_word != word[:len(cur_word)]:
                return
            
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            for direction in directions:
                new_r, new_c = r + direction[0], c + direction[1]
                if 0 <= new_r and new_r < rows and 0 <= new_c and new_c < cols and (new_r, new_c) not in record:
                    record.add((new_r, new_c))
                    dfs(new_r, new_c, cur_word + board[new_r][new_c])
                    record.remove((new_r, new_c))
        
        for r in range(rows):
            for c in range(cols):
                if word[0] == board[r][c]:
                    record.clear()
                    record.add((r, c))
                    dfs(r, c, board[r][c])
                if res:
                    return True
        return False