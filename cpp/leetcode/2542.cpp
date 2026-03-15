// 2542. Maximum Subsequence Score

#include <queue>
#include <vector>
#include <print>
#include <algorithm>

using namespace std;

typedef long long ll;

class Solution {
    public:
    long long maxScore(vector<int> &nums1, vector<int> &nums2, int k){
        int n = nums1.size();
        vector<pair<int,int>> v;

        priority_queue<int> pq;

        ll sum = 0;
        ll ans = 0;

        for (int i = 0; i < n; i++) {
            v.push_back({ nums2[i], nums1[i] });
        }

        sort(v.rbegin(), v.rend());

        for (int i = 0; i < k - 1; i++) {
            sum += v[i].second;
            pq.push(-v[i].second);
        }

        for (int i = k - 1; i < n; i++) {
            sum += v[i].second;
            pq.push(-v[i].second);

            ans = max(ans, sum * v[i].first);

            sum += pq.top();
            pq.pop();
        }


        return ans;
    }

};

struct TestCase {
    vector<int> nums1;
    vector<int> nums2;
    int k;
    int result;
};

int main() {

    Solution s;

    vector<TestCase> testCases = {
        { { 1,3,3,2 }, { 2,1,3,4 }, 3 },
    };

    for (TestCase t: testCases) {
        auto result = s.maxScore(t.nums1, t.nums2, t.k);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
