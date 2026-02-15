// 53. Maximum Subarray

#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
    public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0], currSum = nums[0];

        for (int i = 1; i < nums.size(); i++){
            currSum = max(nums[i], currSum + nums[i]);
            maxSum = max(maxSum, currSum);
        }
        return maxSum;
    }
};

struct TestCase {
    vector<int> nums;
    int expected;
};

int main() {

    vector<TestCase> testCases = {
        {{ -2,1,-3,4,-1,2,1,-5,4 }, 6},
        {{ 1 }, 1},
        {{ 5,4,-1,7,8 }, 23},
    };

    Solution s;
    for (auto t : testCases) {
        auto result = s.maxSubArray(t.nums);
        assert(result == t.expected);
    }

    return 0;
}
