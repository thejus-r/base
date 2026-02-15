// 1. Two Sum
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cassert>

using namespace std;

class Solution {
    public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> m = {};
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (m.count(complement)) {
                return {m[complement], i};
            }
            m[nums[i]] = i;
        }
        return {};
    }
};


int main() {
    Solution s;

    vector<int> nums1 = {2,7,11,15};
    int target1 = 9;

    vector<int> expected1 = {0,1};

    auto result1 = s.twoSum(nums1, target1);

    assert(result1 == expected1);
    cout << "Test passed successfully!" << endl;

    return 0;
}
