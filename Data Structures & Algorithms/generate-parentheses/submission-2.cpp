class Solution {
public:
    vector<string> res;
    void dfs(int openingCount, int closingCount, int n, string& curRes) {
        if (openingCount > n || closingCount > openingCount) {
            return;
        }
        if (openingCount + closingCount == 2*n){
            res.push_back(curRes);
            return;
        }
        curRes.push_back('(');
        dfs(openingCount + 1, closingCount, n, curRes);
        curRes.pop_back();
        curRes.push_back(')');
        dfs(openingCount, closingCount + 1, n, curRes);
        curRes.pop_back();
    }
    vector<string> generateParenthesis(int n) {
        string curRes = "";
        dfs(0, 0, n, curRes);
        return res;
    }
};
