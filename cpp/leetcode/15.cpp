// 15. 3 Sum

#include <cassert>
#include <vector>
#include <algorithm>
#include <print>

using namespace std;

class Solution {
    public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res = {};

        for (int i = 0; i < nums.size(); i++ ) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int l = i + 1, r = nums.size() - 1;
            while (l < r) {

                int threeSum = nums[i] + nums[l] + nums[r];

                if (threeSum > 0) {
                    r -= 1;
                } else if (threeSum < 0) {
                    l += 1;
                } else {
                    res.push_back({ nums[i], nums[l], nums[r] });
                    l += 1;
                    while (nums[l] == nums[l - 1] && l < r) {
                        l += 1;
                    }
                }
            }
        }

        return res;
    };
};

struct TestCase {
    vector<int> nums;
    vector<vector<int>> expected;
};
int main() {

    Solution s;

    vector<TestCase> testCases = {
        { { -1, 0, 1, 2, -1, -4 }, { { -1, -1, 2 }, { -1, 0, 1 } } },
        { { 0, 1, 1 }, { } },
        { { 0, 0, 0 }, { { 0, 0, 0 } } },
        { { -100, -70, -60, 110, 120, 130, 160 }, { { -100, -60, 160 }, { -70, -60, 130 } } }
    };

    for (auto t: testCases) {
        auto result = s.threeSum(t.nums);
        println("{}", result);

        assert(result == t.expected);
    }

}
