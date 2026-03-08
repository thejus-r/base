// 3864. Minimum Cost to Partition a Binary String

#include <algorithm>
#include <cstdlib>
#include <vector>
#include <string>
#include <print>

// Sort anything with n-1, will take atmost 3 ops

using namespace std;

class Solution {
    long long e;
    long long f;
    vector<int> prefix;
    public:
    long long dfs(int left, int right) {
        int L = right - left + 1;
        int X = prefix[right + 1] - prefix[left];

        long long best = 0;

        if (X == 0) {
            best = f;
        } else {
            best = L * X * e;
        }

        if (L % 2 == 0) {
            int mid = left + (right - left) / 2;
            best = min(best, dfs(left, mid) + dfs(mid + 1, right));
        }
        return best;
    }
    long long minCost(string s, int encCost, int flatCost) {
        e = encCost;
        f = flatCost;
        int N = s.length();
        prefix.assign(N + 1, 0);

        // prefix sum
        for (int i = 0; i < N; i++) {
            prefix[i + 1] = prefix[i] + (s[i] == '1');
        }
        return dfs(0, N - 1);
    }
};

struct TestCase {
    string s;
    int encCost;
    int flatCost;
    int result;
};

int main() {
    vector<TestCase> testCases = {
        { "1010", 2, 1, 6 },
    };

    Solution s;

    for (TestCase t: testCases) {
        auto result = s.minCost(t.s, t.encCost, t.flatCost);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
