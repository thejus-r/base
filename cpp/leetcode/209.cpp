// 209. Minimum Size Subarray Sum

#include <algorithm>
#include <climits>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    int minSubArrayLen(int target, vector<int> &nums) {
        int left = 0;

        int res = INT_MAX;
        int curr_sum = 0;

        for (int right = 0; right < nums.size(); right++) {
            curr_sum += nums[right];

            while (curr_sum >= target) {
                res = min(res, right - left + 1);
                curr_sum -= nums[left];
                left++;
            }
        }

        return res == INT_MAX ? 0 : res;
    }

};

struct TestCase {
    vector<int> nums;
    int target;
    int result;
};

int main() {
    vector<TestCase> testCases = {
        { { 2,3,1,2,4,3 }, 7, 2 },
        { { 1,4,4 }, 4, 1 },
    };

    Solution s;
    for (TestCase t: testCases) {
        auto result = s.minSubArrayLen(t.target, t.nums);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
