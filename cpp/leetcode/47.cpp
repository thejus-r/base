// 47. Permutations II

#include <bitset>
#include <vector>
#include <algorithm>
#include <print>

using namespace std;

class Solution {
    public:

    void solve(vector<int> &curr, vector<int> &nums, vector<bool> &used, vector<vector<int>>& res) {
        if (curr.size() == nums.size()) {
            res.push_back(curr);
            return;
        }

        for (int i = 0; i < nums.size(); i++)  {

            if (used[i]) {
                continue;
            }

            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                continue;
            }

            used[i] = true;
            curr.push_back(nums[i]);

            solve(curr, nums, used, res);

            curr.pop_back();
            used[i] = false;
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> curr;

        vector<bool> used(nums.size(), false);

        solve(curr, nums, used, res);

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
        { { 1, 1, 2 } , { { 1, 1, 2 }, { 1, 2, 1 }, { 2, 1, 1 } } },
        { { 1, 2, 3 } , { { 1, 2, 3 }, { 1, 3, 2 }, { 2, 1, 3 }, { 2, 3, 1 }, { 3, 2, 1 }, { 3, 2, 1 } } },
    };

    for (TestCase t: testCases) {
        auto result = s.permute(t.nums);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
