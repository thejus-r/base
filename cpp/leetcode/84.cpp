// 84. Largest Rectangle in Histogram

#include <algorithm>
#include <print>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  int largestRectangleArea(vector<int> &heights) {
    int max_area = 0;

    // since we have to keep track of the shortest height
    // just before the current we use a increasing monotonic stack
    // even if [2, 5]... max height to make reactangle is 2 (width is 1 - 0)
    // so shortest before height will be the blocking factor
    //
    // indexes = [0, 1]
    // heights = [2, 4]
    // stack = [0], max_area = 0;
    // i = 0, idx = , w = , area =

    stack<int> s;

    heights.push_back(0);
    for (int i = 0; i < heights.size(); i++) {

      while (!s.empty() && heights[s.top()] >= heights[i]) {
        // index of shortest height before
        int idx = s.top();
        s.pop();

        int w = s.empty() ? i : i - s.top() - 1;
        int area = w * heights[idx];

        max_area = max(max_area, area);
      }

      s.push(i);
    }

    return max_area;
  }
};

struct TestCase {
  vector<int> heights;
  int result;
};

int main() {
  vector<TestCase> testCases = {
      {{2, 1, 5, 6, 2, 3}, 10},
      {{2, 4}, 4},
      {{1, 1}, 2},
  };

  Solution s;
  for (TestCase t : testCases) {
    auto result = s.largestRectangleArea(t.heights);
    println("Expected: {}, Got: {}", t.result, result);
  }
}
