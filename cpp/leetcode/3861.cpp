// 3861. Minimum Capacity Box

#include <climits>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    int minimumIndex(vector<int>& capacity, int itemSize) {
        int ans = -1;
        int minCapBox = INT_MAX;
        int n = capacity.size();

        for (int i = 0; i < n; i++) {
            if (capacity[i] >= itemSize) {
                if (capacity[i] < minCapBox) {
                    minCapBox = capacity[i];
                    ans = i;
                }
            }
        }

        return ans;
    }
};

struct TestCase {
    vector<int> capacity;
    int itemSize;
    int result;
};

int main() {
    vector<TestCase> testCases = {
        {{ 1, 5, 3, 7 }, 3, 2},
        {{ 3, 5, 4, 3 }, 2, 0},
        {{ 4 }, 5, -1}
    };

    Solution s;

    for (TestCase t: testCases) {
        auto result = s.minimumIndex(t.capacity, t.itemSize);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
