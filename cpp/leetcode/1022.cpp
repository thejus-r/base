// 1022. Sum of Root To Leaf Binary Numbers

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(): val(0), left(nullptr), right(nullptr) {};
  TreeNode(int x): val(x), left(nullptr), right(nullptr) {};
  TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {};
};

class Solution {
    int dfs(TreeNode* node, int currentValue) {
        if (node == nullptr) {
            return 0;
        }

        currentValue = (currentValue << 1) | node->val;

        // leaf node
        if (node->left == nullptr && node-> right == nullptr) {
            return currentValue;
        }

        return dfs(node->left, currentValue) + dfs(node->right, currentValue);
    }
    public:
    int sumRootToLeaf(TreeNode* root) {
        return 0;
    }

};
