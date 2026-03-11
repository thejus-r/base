// 110. Balanced Binary Tree

#include <algorithm>
#include <cstdlib>
#include <utility>

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
    auto dfs(TreeNode* node) -> pair<bool, int> {

        if (node == nullptr) {
            return pair(true, 0);
        }

        auto [ left, h_left ] = dfs(node->left);
        auto [ right, h_right ] = dfs(node->right);

        bool isBalanced = left && right && abs(h_right - h_right) <= 1;

        return pair(isBalanced,1 + max(h_left, h_right));
    }
    public:
    bool isBalanced(TreeNode* root) {
        return dfs(root).first;
    }
};

int main() {

};
