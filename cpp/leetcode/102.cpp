// 102. Binary Tree Level Order Traversal

#include <queue>
#include <vector>

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
    public:
    vector<vector<int>> levelOrder(TreeNode *root) {

        if (root == nullptr){
            return {};
        }
        vector<vector<int>> res = {};

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {

            vector<int> temp;
            int s = q.size();
            for (int i = 0; i < s; i++) {
                TreeNode *curr = q.front(); q.pop();

                if (curr->left != nullptr) {
                    q.push(curr->left);
                }

                if (curr->right != nullptr) {
                    q.push(curr->right);
                }

                temp.push_back(curr->val);
            }

            res.push_back(temp);
        }

        return res;
    }
};
