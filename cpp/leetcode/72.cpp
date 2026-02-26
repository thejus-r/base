// 72. Edit Distance

#include <string>
#include <vector>
#include <print>
#include <algorithm>

using namespace std;

class Solution {
    private:
    // recursive approach, top-down
    int f(int i, int j, string& s, string& t) {

        if (i < 0) {
            return 0;
        }

        if (j < 0) {
            return 1;
        }

        if (s[i] == t[j]) {
            return f(i - 1, j - 1, s, t);
        }

        int ins = 1 + f(i, j - 1, s, t);
        int del = 1 + f(i - 1, j, s, t);
        int rep = 1 + f(i - 1, j - 1, s, t);

        return min({ ins, del, rep });
    }
    public:
    int minDistance(string s, string t) {
        // tabulation, bottom-up

        int m = s.size(), n = t.size();

        vector<int> prev(n + 1, 0);
        vector<int> curr(n + 1, 0);

        for (int i = 0; i <= n; i++) prev[i] = i;

        for (int i = 1; i <= m; i++) {
            curr[0] = i;
            for (int j = 1; j <= n; j++){
                if (s[i - 1] == t[j - 1]) curr[j] = prev[j - 1];
                else {
                    curr[j] = 1 + min({ prev[j], curr[j - 1], prev[j - 1] });
                }
            }

            println("prev: {}", prev);
            println("curr: {}", curr);
            println();
            prev = curr;
        }

        return prev[n];

    }
};

struct TestCase {
    string s;
    string t;
    int result;
};

int main() {

    Solution s;
    vector<TestCase> testCases = {
        { "horse", "ros", 3 },
        // { "intention", "execution", 5 },
    };

    for (TestCase t: testCases) {
        int result = s.minDistance(t.s, t.t);
        println("Expected: {}, Got: {}", t.result, result);
    }
    return 0;
}
