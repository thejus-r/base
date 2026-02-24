// 1461. Check If a String Contains All Binary Codes of Size K

#include <cmath>
#include <string>
#include <print>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
    public:
    bool hasAllCodes(string s, int k) {

        int req = pow(2, k);

        int n = s.size();
        unordered_set<string> unique;

        for (int i = 0; i < n - k + 1; i++) {
            unique.insert(s.substr(i, k));
        }

        println("{} {} {}", unique, unique.size(), req);
        return unique.size() == req;
    }
};

struct TestCase {
    string s;
    int k;
    bool expected;
};

int main() {

    Solution s;

    vector<TestCase>  testCases = {
        { "00110110", 2 , true },
        { "0110", 1 , true },
        { "0110", 2 , false },
        { "00110", 2 , true },

    };

    for (TestCase t: testCases) {
        bool result = s.hasAllCodes(t.s, t.k);
        println("Expected: {}, Got: {}", t.expected, result);
    }

    return 0;
}
