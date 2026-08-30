class Solution {
    public:
        bool isValidSudoku(vector<vector<char>>& board) {
            if (board.empty()){
                return false;
            }
            vector<vector<bool>> row (9, vector<bool>(9, false));
            vector<vector<bool>> col (9, vector<bool>(9, false));
            vector<vector<bool>> grid(9, vector<bool>(9, false));
            for (int r = 0; r < board.size(); r++){
                for (int c = 0; c < board[0].size(); c++){
                    char cur_ch = board[r][c];
                    if (cur_ch == '.'){
                        continue;
                    }
                    if ((row[r][cur_ch - '1']) || (col[c][cur_ch - '1']) || (grid[((r / 3) * 3) + (c / 3)][cur_ch - '1'])){
                        return false;
                    }
                    row[r][cur_ch - '1'] = true;
                    col[c][cur_ch - '1'] = true;
                    grid[((r / 3) * 3) + (c / 3)][cur_ch - '1'] = true;
                }
            }
            return true;
        }
    };