// 20. Valid Parentheses
#include <string>
#include <stack>
#include <unordered_map>
#include <cassert>

using namespace std;

class Solution {
    public:
    bool isValid(string s) {
        stack<char> st = {};
        unordered_map<char, char> m = {{ ')', '(' }, { '}', '{' }, { ']', '[' }};

        for (char c: s) {
            if (m.find(c) == m.end()) {
                st.push(c);
            } else if (!st.empty() && st.top() == m[c]) {
                st.pop();
            } else {
                return false;
            }
        }

        return st.empty();
    }
};

int main() {
    Solution s;
    string s1 = "()[]{}";
    bool expected1 = true;
    auto result1 = s.isValid(s1);
    assert(result1 == expected1);
    return 0;
}
