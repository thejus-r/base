// Length of Longest Subsequence
// DP on String

/*
    * Given two strings str1 and str2, find the length of their longest common subsequence.
    *
    * Input:
    *  str1 = "bdefg", str2 = "bfg"
    *
    * Output:
    * 3
    */

#include <string>
#include <vector>
#include <print>

using namespace std;

// Recursion With Memoization
class Solution1 {
    private:
    int f(int i, int j, string &s, string &t, vector<vector<int>> &dp) {
        // base case, #1
        if (i < 0 || j < 0) return 0;

        if (dp[i][j] != -1) return dp[i][j];

        // base case, #2
        if (s[i] == t[j]) return dp[i][j] = 1 + f(i - 1, j - 1, s, t, dp);

        // max of both branches
        return dp[i][j] = max(f(i - 1, j, s, t, dp), f(i, j - 1, s, t, dp));
    }
    public:
    int longestCommonSubsequence(string s, string t) {
        int n = s.size();
        int m = t.size();

        vector<vector<int>> dp(n, vector<int>(m, -1));

        return f(n - 1, m - 1, s, t, dp);
    }
};

// Tabulation / Bottom Up with 2D DP Array
class Solution2 {
    public:
    int longestCommonSubsequence(string s, string t) {
        int n = s.size();
        int m = t.size();

        vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1));

        for (int i = 0; i <= n; i ++) dp[i][0] = 0;
        for (int j = 0; j <= m; j ++) dp[0][j] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s[i - 1] == t[j - 1]) dp[i][j] = 1 + dp[i - 1][j - 1];
                else dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
            }
        }
        return  dp[n][m];
    }
};

// Tabulation / Bottom Up with Space Optimization
class Solution3 {
    public:
    int longestCommonSubsequence(string s, string t) {
        int n = s.size();
        int m = t.size();
        vector<int> prev(m + 1, 0), curr(m + 1, 0);

        for (int i = 1; i <= n; i ++) {
            for (int j = 1; j <= m; j ++) {
                if (s[i - 1] == t[j - 1]) curr[j] = 1 + prev[j - 1];
                else curr[j] = max(prev[j], curr[j - 1]);
            }


            prev = curr;
        }

        return prev[m];
    }

};

struct TestCase {
    string str1;
    string str2;
    int expected;
};

int main() {
    Solution1 s1;
    Solution2 s2;
    Solution3 s3;

    vector<TestCase> testCases = {
        { "bdefg", "bfg", 3 }
    };

    for (TestCase t: testCases) {
        int result = s1.longestCommonSubsequence(t.str1, t.str2);
        println("Expected: {}, Got: {}",t.expected, result);
    }

    for (TestCase t: testCases) {
        int result = s2.longestCommonSubsequence(t.str1, t.str2);
        println("Expected: {}, Got: {}",t.expected, result);
    }

    for (TestCase t: testCases) {
        int result = s3.longestCommonSubsequence(t.str1, t.str2);
        println("Expected: {}, Got: {}",t.expected, result);
    }

}
