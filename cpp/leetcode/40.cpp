// 40. Combination Sum II

#include <algorithm>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    void solve(int startIdx, vector<int> &candidates, int target, vector<int> &curr, vector<vector<int>> &res) {
        if (target == 0) {
            res.push_back(curr);
            return;
        }

        for (int i = startIdx; i < candidates.size(); i++) {
            if (i > startIdx && candidates[i] == candidates[i - 1]){
                continue;
            }

            if (candidates[i] > target) {
                break;
            }

            curr.push_back(candidates[i]);

            solve(i + 1, candidates, target - candidates[i],curr, res);

            curr.pop_back();
        }


    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target){

        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> curr;

        solve(0, candidates, target, curr, res);
        return res;
    }
};

struct TestCase {
    vector<int> candidates;
    int target;
    vector<vector<int>> result;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { { 10, 1, 2, 7, 6, 1, 5 }, 8, { { 1, 1, 6 }, { 1, 2, 5 }, { 1, 7 }, { 2, 6 } } },
        { { 2, 5, 2, 1, 2 }, 5, { { 1, 2, 2 }, { 5 } } },
    };

    for (TestCase t: testCases) {
        auto result = s.combinationSum2(t.candidates, t.target);

        println("Expected: {}, Got: {}", t.result, result);
    }
}
