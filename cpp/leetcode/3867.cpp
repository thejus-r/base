// 3867. Sum of GCD of Formed Pairs

#include <numeric>
#include <algorithm>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    int gcdSum(vector<int>& nums){
        int n = nums.size();

        vector<int> prefixGcd(n);

        int running_max = nums[0];

        for (int i = 0; i < n; i++) {
            running_max = max(running_max, nums[i]);
            prefixGcd[i] = gcd(nums[i], running_max);
        }

        sort(prefixGcd.begin(), prefixGcd.end());

        int sum = 0;

        int left = 0, right = n - 1;

        while (left < right) {
            sum += gcd(prefixGcd[left], prefixGcd[right]);
            left ++;
            right--;
        }

        return sum;
    }
};

struct TestCase  {
    vector<int> nums;
    long long result;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { { 2, 6, 4 }, 2 },
    };

    for (TestCase t: testCases) {
        auto result = s.gcdSum(t.nums);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
