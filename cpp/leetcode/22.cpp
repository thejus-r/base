// 22. Generate Parentheses

#include <vector>
#include <print>
#include <string>

using namespace std;

class Solution {
    private:
    vector<string> res;

    void backtrack(int open, int close, string curr) {
        if (open == 0 && close == 0) {
            res.push_back(curr);
            return;
        }

        if (open < 0 || close < 0) {
            return;
        }

        if (open > 0) {
            backtrack(open - 1, close, curr + '(');
        }

        if (close > 0 && close > open) {
            backtrack(open, close - 1, curr + ')');
        }

    }

    public:
    vector<string> generateParentheses(int n) {

        backtrack(n, n, "");
        return res;
    }
};


struct TestCase {
  int n;
  vector<string> result;
};

int main() {

    vector<TestCase> testCases = {
        { 3, { "((()))","(()())","(())()","()(())","()()()" } }
    };

    Solution s;

    for (TestCase t: testCases) {
        auto result = s.generateParentheses(t.n);
        println("Expected: {}, Got: {}", t.result, result);
    }

}
