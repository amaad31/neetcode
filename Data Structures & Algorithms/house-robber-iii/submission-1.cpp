/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    pair<int, int> dfs(TreeNode* node){
        if (node == nullptr){
            return {0, 0};
        }
        pair<int, int> left = dfs(node->left);
        pair<int, int> right = dfs(node->right);
        int firstLevel = left.second + right.second + node->val;
        int secondLevel = max(left.second, left.first) + max(right.second, right.first);
        return {firstLevel, secondLevel};
    }
public:
    int rob(TreeNode* root) {
        pair<int, int> res = dfs(root);
        return max(res.first, res.second);
    }
};