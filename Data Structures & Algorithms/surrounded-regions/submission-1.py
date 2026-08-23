class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        not_sur_idx = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))

            while queue:
                row, col = queue.pop()
                for direction in directions:
                    cur_row, cur_col = row + direction[0], col + direction[1]
                    if (
                        0 <= cur_row < rows and
                        0 <= cur_col < cols and
                        board[cur_row][cur_col] == "O" and
                        (cur_row, cur_col) not in visited
                    ):
                        queue.append((cur_row, cur_col))
                        visited.add((cur_row, cur_col))
                        not_sur_idx.add((cur_row, cur_col))


        # first and last rows
        for row in [0, rows - 1]:
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in visited:
                    not_sur_idx.add((row, col))
                    bfs(row, col)
                visited.add((row, col))
        
        # first and last cols
        for row in range(rows):
            for col in [0, cols - 1]:
                if board[row][col] == "O" and (row, col) not in visited:
                    not_sur_idx.add((row, col))
                    bfs(row, col)
                visited.add((row, col))
        
        # replacing the surrounded 'O's with 'X's
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in not_sur_idx:
                    board[row][col] = "X"

    