// 46. Permutations

#include <vector>
#include <algorithm>
#include <print>

using namespace std;

class Solution {
    public:

    void solve(vector<int> &curr, vector<int> &nums, vector<vector<int>> &res) {
        if (curr.size() == nums.size()) {
            res.push_back(curr);
            return;
        }

        for (int n: nums) {
            if (count(curr.begin(), curr.end(), n) == 0) {
                curr.push_back(n);
                solve(curr, nums, res);
                curr.pop_back();
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {

        vector<vector<int>> res;
        vector<int> curr;

        solve(curr, nums, res);

        return res;
    }
};

struct TestCase {
  vector<int> nums;
  vector<vector<int>> result;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { { 1, 2, 3 } , { { 1, 2, 3}, { 1, 3, 2 }, { 2, 1, 3 }, { 2, 3, 1 }, { 3, 1, 2 }, { 3, 2, 1 } } },
        { { 0, 1 } , { { 0, 1 }, { 1, 0 } } },
        { { 1 } , { { 1 } } },
    };

    for (TestCase t: testCases) {
        auto result = s.permute(t.nums);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
