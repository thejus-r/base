// 1758. Minimum Changes To Make Alternating Binary String

#include <string>
#include <print>
#include <vector>

using namespace std;

class Solution {
    public:
    int minOperations(string s) {
        int c1 = 0, c2 = 0;

        for (int i = 0; i < s.size(); i++) {
            char expected1 = (i % 2) == 0 ? '0' : '1';
            char expected2 = (i % 2) == 0 ? '1' : '0';


            if (s[i] != expected1) c1++;
            if (s[i] != expected2) c2++;
        }

        return min(c1, c2);
    }
};

struct TestCase {
    string s;
    int result;
};

int main() {
    vector<TestCase> testCases = {
        { "0100", 1 },
        { "10", 0 },
        { "1111", 2 },
    };

    Solution s;

    for (TestCase t: testCases) {
        auto result = s.minOperations(t.s);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
