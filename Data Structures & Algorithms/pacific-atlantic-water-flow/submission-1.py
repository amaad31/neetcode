class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
             return []
        
        rows, cols = len(heights), len(heights[0]) 
        visited = set()
        status = defaultdict(list) # (r, c) = [<floatToPac>: bool, <floatToAtl>: bool]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(row, col):
            if (row, col) in visited:
                return status[(row, col)]
            cur_res = status[(row, col)]
            visited.add((row, col))
            for direction in directions:
                cur_r, cur_c = row + direction[0], col + direction[1]
                if (
                    0 <= cur_r < rows and
                    0 <= cur_c < cols and
                    heights[cur_r][cur_c] <= heights[row][col]
                ):
                    neighbor_res = dfs(cur_r, cur_c)
                    cur_res[0] = cur_res[0] or neighbor_res[0]
                    cur_res[1] = cur_res[1] or neighbor_res[1]
            status[(row, col)] = cur_res
            return cur_res   
        
        for r in range(rows):
            for c in range(cols):
                status[(r, c)] = [False, False]
                if r == 0 or c == 0:
                    status[(r, c)][0] = True
                if r == rows - 1 or c == cols - 1:
                    status[(r, c)][1] = True

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    dfs(r, c)
        
        res = []
        for k, v in status.items():
            if v == [True, True]:
                res.append(k)
        return res