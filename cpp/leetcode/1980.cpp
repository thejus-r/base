// 1980. Find Unique Binary String

#include <bitset>
#include <string>
#include <unordered_set>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    string findDifferentBinaryString(vector<string>&nums) {

        unordered_set<int> numSet;

        for (string s: nums) {
            numSet.insert(stoi(s, 0, 2));
        }

        int n = nums.size();

        for (int num = 0; num <= n; num++) {
            if (numSet.find(num) == numSet.end()) {
                string ans = bitset<16>(num).to_string();

                return ans.substr(16 - n);
            }
        }

        return "";
    }
};

struct TestCase {
    vector<string> nums;
};

int main() {
    vector<TestCase> testCases = {
        { { "01", "10" } },
    };

    Solution s;

    for (TestCase t: testCases) {
        auto result = s.findDifferentBinaryString(t.nums);
        println("Got: {}", result);
    }
}
