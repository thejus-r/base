// Find the Longest Subsequence
// DP on String

/*
    * Given two strings str1 and str2, find the length of their longest common subsequence.
    *
    * Input:
    *  str1 = "bdefg", str2 = "bfg"
    *
    * Output:
    * "bfg"
    */

#include <string>
#include <vector>
#include <print>

using namespace std;

// Recursion With Memoization
class Solution1 {
    public:
    string longestCommonSubsequence(string s, string t) {
        int m = s.size(), n = t.size();

        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= m; i ++) {
            for (int j = 1; j <= n; j ++) {
                if (s[i - 1] == t[j - 1]) dp[i][j] = 1 + dp[i - 1][j - 1];
                else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        string res = "";

        int i = m, j = n;
        while (i > 0 && j > 0) {
            if (s[i - 1] == t[j - 1]) {
                res = s[i - 1] + res;
                i--; j--;
            } else {
                if (dp[i - 1][j] > dp[i][j - 1]) {
                    i--;
                } else {
                    j--;
                }
            }
        }

        return res;
    }
};

struct TestCase {
    string str1;
    string str2;
    string expected;
};

int main() {
    Solution1 s1;

    vector<TestCase> testCases = {
        { "abcde", "bdqek", "bde" },
        { "abcdeq", "bcdeaq", "bcdeq" }
    };

    for (TestCase t: testCases) {
        string result = s1.longestCommonSubsequence(t.str1, t.str2);
        println("Expected: {}, Got: {}",t.expected, result);
    }
}
