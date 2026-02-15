// 242. Valid Anagram

#include <string>
#include <cassert>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq = {};

        for (char c: s) {
            freq[c]++;
        }

        for (char c: t) {
            freq[c]--;
        }

        for (auto i: freq) {
            if (i.second != 0) {
                return false;
            }
        }

        return true;
    }
};

struct TestCase {
    string s;
    string t;
    bool expected;
};

int main() {

    Solution s;

    vector<TestCase> testCases = {
        { "anagram", "nagaram", true },
        { "rat", "car", false},
    };

    for (TestCase test: testCases) {
        auto result = s.isAnagram(test.s, test.t);
        assert(result == test.expected);
    }

    return 0;
}
