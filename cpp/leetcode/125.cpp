// 125. Valid Palindrome

#include <cassert>
#include <string>
#include <vector>
#include <cctype>

using namespace std;
class Solution {
    public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;

        while (left < right) {
            while (!isalnum(s[left]) && left < right) {
                left++;
            }
            while (!isalnum(s[right]) && right > left) {
                right--;
            }

            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
};

struct TestCase {
    string input;
    bool expected;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        {"A man, a plan, a canal: Panama", true},
        {"race a car", false},
        {" ", true},
    };

    for (const auto& test: testCases) {
        auto result1 = s.isPalindrome(test.input);
        assert(result1 == test.expected);
    }
}
