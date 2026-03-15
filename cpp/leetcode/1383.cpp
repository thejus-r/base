// 1383. Maximum Performance of a Team

#include <queue>
#include <vector>
#include <algorithm>
#include <print>

using namespace std;

class Solution {
    public:
    int maxPerformance(int n, vector<int> &speed, vector<int> &efficiency, int k) {

        int MOD = 1e9 + 7;

        // to find min efficiency, we sort it decreasing
        vector<pair<int, int>> v;

        for (int i = 0; i < n; i++) {
            v.push_back({ efficiency[i], speed[i] });
        }

        sort(v.rbegin(), v.rend());

        long long ans = 0;
        long long sum = 0;

        priority_queue<int> pq;

        for (int i = 0; i < n; i++) {
            sum += v[i].second;
            pq.push(-v[i].second);

            ans = max(ans, sum * v[i].first);

            if ( i >= k - 1) {
                sum += pq.top();
                pq.pop();
            }
        }

        return ans % MOD;
    }
};

struct TestCase {
  int n;
  vector<int> speed;
  vector<int> efficiency;
  int k;
  int result;
};

int main() {

    Solution s;
    vector<TestCase> testCases = {
        { 6, { 2,10,3,1,5,8 }, { 5,4,3,9,7,2 }, 2, 60 },
        { 3, { 2,8,2 }, { 2,7,1 }, 2, 56 }
    };

    for (TestCase t: testCases) {
        auto result = s.maxPerformance(t.n, t.speed, t.efficiency, t.k);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
