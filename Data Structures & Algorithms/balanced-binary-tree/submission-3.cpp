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
    bool res = true;
    int bfs(TreeNode* curNode){
        if (curNode == nullptr){
            return 0;
        }
        int left = bfs(curNode->left);
        int right = bfs(curNode->right);
        if (abs(left - right) >= 2) {
            res = false;
        }
        return 1 + max(left, right);
    }
public:
    bool isBalanced(TreeNode* root) {
        bfs(root);
        return res;
    }
};
