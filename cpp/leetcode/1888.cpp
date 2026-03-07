// 1888. Minimum Number of Flips to Make the Binary String Alternating

/*
 *          ---
 * 1010 -> 10101010
 *
 */

#include <vector>
#include <string>
#include <print>

using namespace std;

class Solution {
    public:
    int minOperations(string s) {
        int op[2] = {0, 0};
        for (int i = 0; i < s.length(); i++) {
            op[(s[i] ^ i) & 1]++;
        }
        return min(op[0], op[1]);
    }
    int minFlips(string s) {
        int n = s.length();

        int op[2] = {0, 0};
        for (int i = 0; i < n; i++) {
            op[(s[i] ^ i) & 1]++;
        }

        int res = min(op[0], op[1]);

        for (int i = 0; i < n - 1; i++) {
            op[(s[i] ^ i) & 1]--;
            op[(s[i] ^ (n + i)) & 1]++;

            res = min(res, min(op[0], op[1]));
        }

        return res;
    }
};

struct TestCase {
    string s;
    int result;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { "111000", 2 },
        // { "101", 0 },
        // { "1110", 1 },
    };

    for (TestCase t: testCases) {
        auto result = s.minFlips(t.s);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
