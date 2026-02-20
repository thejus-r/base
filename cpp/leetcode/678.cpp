// 678. Valid Parenthesis String
#include <string>
#include <vector>
#include <print>

using namespace std;

class Solution {
    private:
        bool isValidString(int index, int openCount, const string &str, vector<vector<bool>> &memo) {
            if (index == str.size()) {
                return (openCount == 0);
            }

            if (memo[index][openCount]) {
                return memo[index][openCount];
            }

            bool isValid = false;

            if (str[index] == '*') {
                isValid |= isValidString(index + 1, openCount + 1, str, memo); // * as '('

                if (openCount) {
                    isValid |= isValidString(index + 1, openCount - 1, str, memo);
                }
                isValid |= isValidString(index + 1, openCount,str, memo);
            } else {
                if (str[index] == '(') {
                    isValid = isValidString(index + 1, openCount + 1, str, memo);
                } else if (openCount) {
                    isValid = isValidString(index + 1, openCount - 1, str, memo);
                }

            }

            return memo[index][openCount] = isValid;
        }
    public:
    bool checkValidString(string s) {
        vector<vector<bool>> memo(s.size(), vector<bool>(s.size(), false));
        return isValidString(0, 0, s, memo);
    }
};

struct TestCase {
    string s;
    bool expected;
};

int main() {

    vector<TestCase> testCases = {
        { "(*)", true },
        { "(*))", true },
        { "*****))", true },
    };

    Solution s;
    for (TestCase t: testCases) {
        bool result = s.checkValidString(t.s);
        println("Input: {}, Expected: {}, Result: {}", t.s, t.expected, result);
    }

    return 0;
}
