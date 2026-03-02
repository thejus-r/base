// 3852. Smallest Pair with Different Frequencies

#include <map>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    vector<int> minDistinctFreqPair(vector<int> &nums) {
        map<int, int> freq_map;

        for (int n: nums) {
            freq_map[n]++;
        }

        vector<int> unique_nums;

        for (const auto [k, v]: freq_map) {
            unique_nums.push_back(k);
        }

        for (int i = 0; i < unique_nums.size(); i++) {
            int x = unique_nums[i];
            for (int j = i + 1; j < unique_nums.size(); j++) {
                int y = unique_nums[j];

                if (freq_map[x] != freq_map[y]) {
                    return { x, y };
                }
            }
        }

        return { -1, -1 };
    }

};

struct TestCase {
    vector<int> nums;
    vector<int> result;
};

int main() {

    Solution s;

    vector<TestCase> testCases = {
      { { 1, 1, 2, 2, 3, 4 }, { 1, 3 } },
      { { 1, 5 }, { -1, -1 } }
    };

    for (TestCase t: testCases) {
        auto result = s.minDistinctFreqPair(t.nums);
        println("Expected: {}, Got: {}", t.result, result);
    }

}
