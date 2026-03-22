// 3877. Minimum Removals to Achieve Target XOR

/*
 *
 */

#include <print>
#include <queue>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  int minRemovals(vector<int> &nums, int target) {
    int sum = 0;

    for (int n : nums) {
      sum ^= n;
    }

    // we try to reverse it, by finding min no of elements
    // needed to cancel out from the total xor sum, to reach the target
    int required = sum ^ target;

    if (required == 0)
      return 0;

    // taking only unique numbers as x ^ x = 0, so x ^ x ^ x = x
    unordered_set<int> unique_numbers(nums.begin(), nums.end());

    // we keep track of <curr xor sum, numbers removed>
    queue<pair<int, int>> q;
    unordered_set<int> visited;

    q.push({0, 0});
    visited.insert(0);

    while (!q.empty()) {
      auto [curr_sum, removed] = q.front();
      q.pop();

      for (int n : unique_numbers) {
        int next_sum = curr_sum ^ n;

        if (next_sum == required) {
          return removed + 1;
        }

        if (!visited.contains(next_sum)) {
          q.push({next_sum, removed + 1});
          visited.insert(next_sum);
        }
      }
    }

    return -1;
  }
};

struct TestCase {
  vector<int> nums;
  int target;
  int result;
};

int main() {
  vector<TestCase> testCases = {
      {{1, 2, 3}, 2, 1},
      {{2, 4}, 1, -1},
      {{7}, 7, 0},
  };

  Solution s;
  for (TestCase t : testCases) {
    auto result = s.minRemovals(t.nums, t.target);
    println("Expected: {}, Got: {}", t.result, result);
  }
}
