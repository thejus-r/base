// 761. Special Binary String

#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    string makeLargestSpecial(string s){
        if (s.size() <= 2) {
            return s;
        }
        int start = 0;
        int balance = 0;
        vector<string> mountains;

        for (int i = 0; i < s.size(); i ++) {
            if (s[i] == '1') {
                balance++;
            } else {
                balance--;
            }

            if (balance == 0) {
                string inner_string = s.substr(start + 1, i - start - 1);

                string processed_inner = makeLargestSpecial(inner_string);

                mountains.push_back("1" + processed_inner + "0");

                start = i + 1;
            }
        }

        sort(mountains.begin(), mountains.end(), greater<string>());


        string result = "";
        for (const string& mountain: mountains) {
            result += mountain;
        }

        return result;
    }
};

struct TestCase  {
    string s;
    string r;
};

int main() {

    Solution s;
    vector<TestCase> testCases = {
        { "11011000", "11100100" },
        { "10", "10" },
    };

    for (TestCase t: testCases) {
        string result = s.makeLargestSpecial(t.s);
        println("Input: {}, Expected: {}, Got: {}",t.s ,t.r, result);
    }
}
