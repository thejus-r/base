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
        return "";
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
        { "bdefg", "bfg", "bfg" }
    };

    for (TestCase t: testCases) {
        string result = s1.longestCommonSubsequence(t.str1, t.str2);
        println("Expected: {}, Got: {}",t.expected, result);
    }
}
