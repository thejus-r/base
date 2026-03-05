// 94. Binary Tree Inorder Traversal

#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(): val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right): val(x), left(left), right(right) {}
};

class Solution {
    private:
    void inorder(TreeNode *node, vector<int> &res) {
        if (node == nullptr) {
            return;
        }

        inorder(node->left, res);
        res.push_back(node->val);
        inorder(node->right, res);

    }
    public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> res;
        return res;
    }
};

int main() {

}
