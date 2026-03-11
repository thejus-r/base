// 543. Diameter of Binary Tree

#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(): val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right): val(x), left(left), right(right) {}
};

class Solution {
    private:
    int longest = 0;

    int dfs(TreeNode* node) {

        if (node == nullptr) {
            return 0;
        }

        int h_left = dfs(node->left);
        int h_right = dfs(node->right);

        longest = max(longest, h_left + h_right);

        return 1 + max(h_left, h_right);
    }

    public:
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return longest;
    }
};
