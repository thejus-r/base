// 973. K Closest Points to Origin

#include <algorithm>
#include <cassert>
#include <functional>
#include <utility>
#include <vector>
#include <print>
#include <queue>

using namespace std;
using Element = pair<int, pair<int, int>>;
// Euclidean distance between origin and point
// sqrt ( (x1-x2)^2 + (y1-y2)^2 )
// sqrt ( x1^2 + y1^2 ) -> origin is (0, 0)
class Solution {
    public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {

        priority_queue<Element, vector<Element>, greater<Element>> minHeap;

        for (auto p: points) {
            int x = p[0], y = p[1];
            minHeap.push({ x*x + y*y, { x, y }});
        }

        vector<vector<int>> res;
        int i = 0;
        int heapSize = minHeap.size();
        while (i < min(k, heapSize)) {
            auto el = minHeap.top(); minHeap.pop();
            res.push_back({ el.second.first, el.second.second });
            i ++;
        }

        return res;
    }

};

struct TestCase {
    vector<vector<int>> points;
    int k;
    vector<vector<int>> expected;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { { { 1, 3 }, { -2, 2 } }, 1, { { -2, 2 } } },
        { { { 3, 3 }, { -5, 1 }, { -2, 4 } }, 2, { { 3, 3 }, { -2, 4 } } },
    };

    for (auto t: testCases) {
        auto result = s.kClosest(t.points, t.k);
        println("{}", result);
        assert(result == t.expected);
    }
}
