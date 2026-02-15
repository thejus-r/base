// 704. Binary Search

#include <vector>
#include <cassert>

using namespace std;
class Solution {
    public:
    int search(vector<int> &nums, int target) {
        int lo = 0, hi = nums.size() - 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }

        }

        return -1;
    }
};

struct TestCase {
    vector<int> input;
    int target;
    int expected;
};

int main() {

    Solution s;

    vector<TestCase> testCases = {
        {{-1,0,3,5,9,12}, 9, 4 },
        {{-1,0,3,5,9,12}, 2, -1 }
    };

    for (auto t: testCases) {
        auto result = s.search(t.input, t.target);
        assert(result == t.expected);
    }
    return 0;
}
