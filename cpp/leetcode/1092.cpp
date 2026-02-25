// 1092. Shortest Common Supersequence

/*
 * Intuition:
 * We find the lcs and build the supersequence string
 */

#include <algorithm>
#include <string>
#include <vector>
#include <print>

using namespace std;

class Solution {
    private:
    string lcs(string& s, string& t) {
        int m = s.size(), n = t.size();

        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) dp[i][j] = 1 + dp[i - 1][j - 1];
                else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        int i = m, j = n;

        string result = "";

        while (i > 0 && j > 0) {
            // equal
            if (s[i - 1] == t[j - 1]) {
                result += s[i - 1];
                i--; j--;
            } else {
                // not equal characters
                if (dp[i - 1][j] > dp[i][j - 1]) {
                    result += s[i - 1];
                    i--;
                } else {
                    result += t[j - 1];
                    j--;
                }
            }
        }

        while (i > 0) {
            result += s[i - 1];
            i--;
        }

        while (j > 0) {
            result += t[j - 1];
            j--;
        }

        reverse(result.begin(), result.end());

        return result;
    }
    public:
    string shortestCommonSupersequence(string str1, string str2) {
        string long_string = lcs(str1, str2);
        return long_string;
    };
};

struct TestCase {
    string str1;
    string str2;
    string result;
};

int main() {

    vector<TestCase> testCases = {
        // { "abac", "cab", "cabac" },
        // { "aaaaaaaa", "aaaaaaaa", "aaaaaaaa" },
        { "bbbaaaba", "bbababbb", "bbbaaababbb" }
    };

    Solution s;

    for (TestCase t: testCases) {
        string result = s.shortestCommonSupersequence(t.str1, t.str2);
        println("Expected: {}, Got: {}", t.result, result);
    }
    return 0;
}
