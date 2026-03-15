// 3868. Minimum Cost to Equalize Arrays Using Swaps

#include <unordered_map>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    int minCost(vector<int>& nums1, vector<int>& nums2){

        unordered_map<int, int> count1;
        unordered_map<int, int> total_count;

        for (int n: nums1) {
            count1[n]++;
            total_count[n]++;
        }
        for (int n: nums2) {
            total_count[n]++;
        }

        int swaps = 0;

        for (auto [num, total_freq]: total_count) {
            if (total_freq % 2 != 0) {
                return -1;
            }

            int target_freq = total_freq / 2;

            if (count1[num] > target_freq) {
                swaps += (count1[num] - target_freq);
            }
        }


        return swaps;
    }
};

struct TestCase  {
    vector<int> nums1;
    vector<int> nums2;
    int result;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { { 10, 20 }, { 20, 10 }, 0 },
        { { 10, 10 }, { 20, 20 }, 1 },
        { { 10, 20 }, { 30, 40 }, -1 },
    };

    for (TestCase t: testCases) {
        int result = s.minCost(t.nums1, t.nums2);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
