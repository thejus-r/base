// 1143. Longest Common Subsequence

#include <string>
#include <vector>
#include <print>

using namespace std;

class Solution {
    private:

    // Recursion with Memoization
    // int f(int i, int j, string &s, string &t, vector<vector<int>> &memo) {

    //     if (i < 0 || j < 0) return 0;

    //     if (memo[i][j] != -1) return memo[i][j];

    //     if (s[i] == t[j]) return memo[i][j] = 1 + f(i - 1, j - 1, s, t, memo);
    //     else {
    //         return memo[i][j] = max(f(i - 1, j, s, t, memo), f(i, j - 1, s, t, memo));
    //     }
    // }

    public:
    int longestCommonSubsequence(string s, string t) {
        int m = s.size(), n = t.size();

        // Recursion with Memoization
        // vector<vector<int>> memo(n, vector<int>(m, -1));
        // return f(m - 1, n - 1, s, t, memo);

        // Tabulation or Bottom Up
        // vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        // for (int i = 1; i <= m; i++) {
        //     for (int j = 1; j <= n; j++) {
        //         if (s[i - 1] == t[j - 1]) dp[i][j] = 1 + dp[i - 1][j - 1];
        //         else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        //     }
        // }

        // return dp[m][n];

        // Space Optimized Tabulation
        vector<int> prev(n + 1, 0), curr(n + 1, 0);

        for (int i = 1; i <= m; i ++) {
            for (int j = 1; j <= n; j ++){
                if (s[i - 1] == t[j - 1]) curr[j] = 1 + prev[j - 1];
                else curr[j] = max(curr[j - 1], prev[j]);
            }

            prev = curr;
        }

        return prev[n];
    }

};

struct TestCase {
    string s;
    string t;
    int expected;
};

int main(){

    vector<TestCase> testCases = {
        { "abcde", "ace", 3 },
        { "abc", "abc", 3 },
        { "abc", "def", 0 },
    };

    Solution s;

    for (TestCase t: testCases) {
        int result = s.longestCommonSubsequence(t.s, t.t);
        println("Expected: {}, Got: {}", t.expected, result);
    }

    return 0;
}
