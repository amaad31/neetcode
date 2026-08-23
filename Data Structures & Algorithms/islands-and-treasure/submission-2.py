class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    queue.append(((r, c), 0))

        directions = [(0, 1),(0, -1), (1, 0), (-1, 0)]
        while queue:
            cur_node, cur_dis = queue.popleft()
            grid[cur_node[0]][cur_node[1]] = cur_dis
            for direction in directions:
                cur_r, cur_c = cur_node[0] + direction[0], cur_node[1] + direction[1]
                if (0 <= cur_r < rows 
                and 0 <= cur_c < cols 
                and grid[cur_r][cur_c] != -1 
                and (cur_r, cur_c) not in visited 
                and grid[cur_r][cur_c] >= 1):
                    queue.append(((cur_r, cur_c), cur_dis + 1))
                    visited.add((cur_r, cur_c))
