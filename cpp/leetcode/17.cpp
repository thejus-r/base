// 17. Letter Combinations of a Phone Number

#include <unordered_map>
#include <vector>
#include <string>
#include <print>

using namespace std;
class Solution {
    int size;
    vector<string> res;
    string digits;

    unordered_map<char, string> map = {
        { '2', "abc" },
        { '3', "def" },
        { '4', "ghi" },
        { '5', "jkl" },
        { '6', "mno" },
        { '7', "pqrs" },
        { '8', "tuv" },
        { '9', "wxyz" },
    };
    public:
    void f(int idx, string curr) {
        if (idx == digits.length()) {
            res.push_back(curr);
            return;
        }

        for (char c: map[digits[idx]]) {
            f(idx + 1, curr + c);
        }

    }
    vector<string> letterCombinations(string digits) {
        this->digits = digits;
        this->size = digits.length();

        f(0, "");

        return res;
    }
};

struct TestCase {
    string digits;
    vector<string> result;
};

int main() {

    vector<TestCase> testCases = {
      { "23", { "ad","ae","af","bd","be","bf","cd","ce","cf" } },
    };

    Solution s;
    for (TestCase t: testCases) {
        auto result = s.letterCombinations(t.digits);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
