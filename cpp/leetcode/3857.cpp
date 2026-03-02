// 3857. Minimum Cost to Split into Ones

#include <cstring>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    int dp[600];
    int solve(int n) {
        if (n == 1) return 0;

        if (dp[n] != -1) return dp[n];

        int cost = 1e9;
        for (int i = 1; i <= (n / 2); i++) {
            int x = i; int y = (n - i);

            int temp_cost = x * y + solve(x) + solve(y);
            cost = min(temp_cost, cost);
        }

        return dp[n] = cost;

    }
    int minCost(int n) {
        memset(dp, -1, sizeof(dp));
        return solve(n);
    }
};

struct TestCase {
  int n;
  int result;
};

int main() {

    Solution s;
    vector<TestCase> testCases = {
        { 3, 3 },
        { 4, 6 },
    };

    for (TestCase t: testCases) {
        auto result = s.minCost(t.n);
        println("Expected: {}, Got: {}", t.result, result);
    }
    return 0;
}
