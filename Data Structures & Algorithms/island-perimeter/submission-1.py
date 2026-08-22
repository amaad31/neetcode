class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(row, col):
            cur_res = 0
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while queue:
                r, c = queue.popleft()
                cur_res += 4
                for direction in directions:
                    cur_r, cur_c = r + direction[0], c + direction[1]
                    if 0 <= cur_r < rows and 0 <= cur_c < cols and grid[cur_r][cur_c] == 1:
                            cur_res -= 1
                            if (cur_r, cur_c) not in visited:
                                visited.add((cur_r, cur_c))
                                queue.append((cur_r, cur_c))
            
            return cur_res

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res += bfs(r, c)
        
        return res