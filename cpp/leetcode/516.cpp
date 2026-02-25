// 516. Longest Palindromic Subsequence

#include <algorithm>
#include <vector>
#include <string>
#include <print>

using namespace std;
class Solution {
    public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();

        string t = s;
        reverse(t.begin(), t.end());

        auto lcs = [](string &s, string &t) -> int {
            int m = s.size();
            int n = t.size();

            vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

            for (int i = 1; i <= m; i++) {
                for (int j = 1; j <= n; j++) {
                    if (s[i - 1] == t[j - 1]) dp[i][j] = 1 + dp[i-1][j-1];
                    else dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }

            return dp[m][n];
        };

        return lcs(s, t);
    }

};

struct TestCase {
    string s;
    int result;
};

// Driver code
int main() {

    Solution s;

    vector<TestCase> testCases = {
        { "bbbab", 4 },
        { "cbbd", 2 },
    };

    for (TestCase t: testCases) {
        int result = s.longestPalindromeSubseq(t.s);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
