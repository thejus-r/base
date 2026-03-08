// 3862. Find the Smallest Balanced Index

#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    int smallestBalancedIndex(vector<int>& nums) {
        int N = nums.size();
        vector<int> p(nums.begin(), nums.end()), s(nums.begin(), nums.end());
        int ans = -1;

        // prefix sum (s)
        for (int i = 1; i < N; i++) {
            s[i] += s[i - 1];
        }

        for (int i = N - 2; i >= 0; i--) {
            p[i] *= p[i + 1];
        }

        for (int i = 0; i < N; i++) {
            int l = i - 1 >= 0 ? s[i - 1] : 0;
            int r = i + 1 < N ? p[i + 1] : 1;

            if (l == r) {
                ans = i;
                break;
            }

        }


        return ans;
    }
};

struct TestCase {
    vector<int> nums;
    int result;
};

int main() {
    vector<TestCase> testCases = {
        {{ 2, 1, 2 }, 1},
    };

    Solution s;

    for (TestCase t: testCases) {
        auto result = s.smallestBalancedIndex(t.nums);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
