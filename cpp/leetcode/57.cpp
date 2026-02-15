// 57. Insert Interval

#include <cassert>
#include <vector>
#include <print>
using namespace std;

class Solution {
    public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        int n = intervals.size();
        int i = 0;

        while (i < n && intervals[i][1] < newInterval[0]) {
            res.push_back(intervals[i]);
            i++;
        }

        while (i < n && newInterval[1] >= intervals[i][0]) {
            newInterval[0] = min(intervals[i][0], newInterval[0]);
            newInterval[1] = max(intervals[i][1], newInterval[1]);
            i++;
        }
        res.push_back(newInterval);

        while (i < n) {
            res.push_back(intervals[i]);
            i++;
        }


        println("{}",res);
        return res;
    }
};

struct TestCase {
    vector<vector<int>> intervals;
    vector<int> newInterval;
    vector<vector<int>> expected;
};

int main() {

    vector<TestCase> testCases = {
        { { { 1, 3 }, { 6, 9 } }, { 2, 5 }, { { 1, 5 }, { 6, 9 } } },
        { { { 1, 2 }, { 3, 5 }, { 6, 7 }, { 8, 10 }, { 12, 16 } }, { 4, 8 }, { { 1, 2 }, { 3, 10 }, { 12, 16 } } },
    };

    Solution s;

    for (auto t: testCases) {
        auto result = s.insert(t.intervals, t.newInterval);
        assert(result == t.expected);
    }

    return 0;
}
