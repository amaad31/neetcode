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
    int res = 0;
    int dfs(TreeNode* curNode){
        if (curNode == nullptr){
            return 0;
        }
        int leftDepth = dfs(curNode->left);
        int rightDepth = dfs(curNode->right);
        res = max(res, leftDepth + rightDepth);
        return 1 + max(rightDepth, leftDepth);
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int tmpRes = dfs(root);
        return res;
    }
};
