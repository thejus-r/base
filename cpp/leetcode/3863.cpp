// 3863. Minimum Operations to Sort a String

#include <algorithm>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    int minOperations(string s) {
        string sorted_s = s;
        sort(sorted_s.begin(), sorted_s.end());

        // already sorted
        if (s == sorted_s) {
            return 0;
        }

        int N = s.length();

        // unable to sort 2 char string
        if (N == 2) {
            return -1;
        }


        // can sort with 1 op
        if (s[0] == sorted_s[0] || s[N - 1] == sorted_s[N - 1]) {
            return 2;
        }

        // 3 swap case
        char min_char = sorted_s[0];
        char max_char = sorted_s[N - 1];

        int min_count = count(s.begin(), s.end(), min_char);
        int max_count = count(s.begin(), s.end(), max_char);

        if (s[0] == max_char && max_char == 1 && s[N - 1] == min_char && min_count == 1) {
            return 3;
        }


        return 2;
    }
};

struct TestCase {
    string s;
    int result;
};

int main() {
    vector<TestCase> testCases = {
        { "dog", 1 },
        { "card", 2 },
    };

    Solution s;

    for (TestCase t: testCases) {
        auto result = s.minOperations(t.s);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
