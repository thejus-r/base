// 1249. Minimum Remove to Make Valid Parentheses

#include <stack>
#include <string>
#include <vector>
#include <print>

using namespace std;

/*
 * Intuition, we precompute the open and closed parantheses
 * we rebuild the string
 */
class Solution {
    public:
    string minRemoveToMakeValid(string s) {
        int open = 0, close = 0, flag = 0;

        // pass 1
        // we calculate open count & close count (if there is open > close)
        for (char c: s) {
            if (c == '(') {
                open++;
                flag++;
            }

            // flag should be greater than 0
            if (c == ')' && flag > 0){
                close++;
                flag--;
            }
        }

        open = close = min(open, close);

        string res = "";
        for (char c: s) {
            if (c == '(') {
                if (open > 0) {
                    res+= c;
                    open--;
                }
            }
            else if (c == ')') {
                if (close > 0 && close > open) {
                    res+= c;
                    close--;
                }
            } else {
                res += c;
            }
        }
        return res;
    }

};

struct TestCase {
    string s;
    string result;
};

int main(){

    Solution s;
    vector<TestCase> testCases = {
        { "lee(t(c)o)de)", "lee(t(c)o)de" },
        { "a)b(c)d", "ab(c)d" },
        { "))((", "" },
    };

    for (TestCase t: testCases) {
        auto result = s.minRemoveToMakeValid(t.s);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
