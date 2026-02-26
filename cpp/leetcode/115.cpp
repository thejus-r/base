// 115. Distinct Subsequences

#include <string>
#include <vector>
#include <print>

using namespace std;

class Solution {
  public:
    int numDistinct(string s, string t) {
        int m = s.size(), n = t.size();

        // vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        vector<int> prev(n + 1, 0);
        vector<int> curr(n + 1, 0);

        prev[0] = curr[0] = 1;

        for (int i = 1; i <= m; i ++) {
            for (int j = 1; j <= n; j ++) {
                if (s[i - 1] == t[j - 1]) curr[j] = prev[j - 1] + prev[j];
                else curr[j] = prev[j];
            }
            prev = curr;
        }

        return prev[n];

  }
};

struct TestCase {
    string s;
    string t;
    int result;
};

int main() {

    Solution s;

    vector<TestCase> testCases = {
        // { "rabbbit", "rabbit", 3 },
        { "babgbag", "bag", 5 },
    };

    for (TestCase t: testCases) {
        int result = s.numDistinct(t.s, t.t);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
