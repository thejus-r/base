// 39. Combination Sum

#include <vector>
#include <print>

using namespace std;

class Solution {
    private:
    vector<vector<int>> res;

    void backtrack(int idx, vector<int>curr, vector<int>& candidates, int target) {

        // Good Base Case
        if (target == 0) {
            res.push_back(curr);
            return;
        }

        // Bad Base Case
        if (target < 0 || idx >= candidates.size()) {
            return;
        }

        curr.push_back(candidates[idx]);
        // taking curr index
        backtrack(idx, curr, candidates, target - candidates[idx]);

        curr.pop_back();
        // skipping curr index
        backtrack(idx + 1, curr, candidates, target);
    }
    public:
    vector<vector<int>> combinationSum(vector<int> candidates, int target) {
        res = {};
        backtrack(0, {}, candidates, target);
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
        { { 2, 3, 6, 7 }, 7, { { 2, 2, 3 }, { 7 } } },
        { { 2, 3, 5 }, 8, { { 2, 2, 2, 2 }, { 2, 3, 3 }, { 3, 5 } } },
    };

    for (TestCase t: testCases) {
        auto result = s.combinationSum(t.candidates, t.target);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
