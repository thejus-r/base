// 44. Wildcard Matching

#include <string>
#include <vector>
#include <print>
#include <cassert>

using namespace std;

class Solution {
    private:
    // i -> index of text
    // j -> index of pattern
    bool f(int i, int j, string &text, string &pattern, vector<vector<int>> &dp)
    {
        // base case: both equally match
        if (i == 0 && j == 0) {
            return true;
        }
        // base case: pattern is exausted, but text is left
        if (j == 0 && i > 0) {
            return false;
        }

        // base case: text is exausted, pattern is left
        if (i == 0 && j > 0) {
            // pattern[j] should be "*", for ""
            for (int ii = 1; ii <= j; ii ++) {
                if (pattern[ii - 1] != '*') {
                    return false;
                }
            }

            return true;
        }

        if (dp[i][j] != -1) return dp[i][j];

        // matching letters or '?'
        if (text[i - 1] == pattern[j - 1] || pattern[j - 1] == '?') {
            return dp[i][j] = f(i - 1, j - 1, text, pattern, dp);
        }

        if (pattern[j - 1] == '*') {
            // we have two choices, use '*' or skip
            return dp[i][j] = f(i - 1, j, text, pattern, dp) || f(i , j - 1 , text, pattern, dp);
        }

        return dp[i][j] = false;
    }
    public:
    bool isMatch(string text, string pattern) {
        int m = text.size(), n = pattern.size();

        vector<int> prev(m + 1, false), curr(m + 1, false);

        prev[0] = true;

        for (int i = 1; i <= n; i++) {
            bool flag = true;

            for (int ii = 1; ii <= n; ii++) {
                if (pattern[ii - 1] != '*') {
                    flag = false;
                    break;
                }
            }

            curr[0] = flag;

            for (int j = 1; j <= m; j ++) {
                if (pattern[i - 1] == text[j - 1] || pattern[i - 1] == '?') {
                    curr[j] = prev[j - 1];
                } else if (pattern[i - 1] == '*') {
                    curr[j] = prev[j] | curr[j -1];
                } else {
                    curr[j] = false;
                }

                prev = curr;
            }
        }


        return prev[n];
    }
};

struct TestCase {
    string text;
    string pattern;
    bool result;
};

int main() {

    vector<TestCase> testCases = {
        // { "aa", "a", false },
        // { "aa", "*", true },
        // { "cb", "?a", false },
        // { "acb", "a*b", true },
        { "acb", "*b", true },
        // { "acb", "a?b", true },
        // { "acb", "ac?b", false},
        // { "acb", "*", true },
        // { "acb", "v", false},
        // { "acb", "???", true},
        // { "mississippi", "m??*ss*?i*pi", false},

    };

    Solution s;

    for (TestCase t: testCases){
        bool result = s.isMatch(t.text, t.pattern);
        println("Expected: {}, Got: {}", t.result, result);
        // assert(result == t.result);
    }
    return 0;
}
