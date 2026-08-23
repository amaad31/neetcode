class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]

            while queue:
                row, col = queue.popleft()
                for direction in directions:
                    cur_r, cur_c = row + direction[0], col + direction[1]
                    if (
                        0 <= cur_r < rows and
                        0 <= cur_c < cols and
                        grid[cur_r][cur_c] == "1" and
                        (cur_r, cur_c) not in visited
                    ):
                        queue.append((cur_r, cur_c))
                        visited.add((cur_r, cur_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        
        return res