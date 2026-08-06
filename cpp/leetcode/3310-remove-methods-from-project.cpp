// 3310. Remove Methods from Project
// Medium

#include <print>
#include <queue>
#include <vector>

using namespace std;
class Solution {
public:
  vector<int> remainingMethods(int n, int k, vector<vector<int>> &invocations) {

    // Step 1:
    // Build adjency list for the directed graph
    vector<vector<int>> adj(n);

    for (auto &edge : invocations) {
      int caller = edge[0];
      int reciever = edge[1];

      adj[caller].push_back(reciever);
    }

    queue<int> q;
    vector<bool> suspicious(n, false);

    q.push(k);
    suspicious[k] = true;

    while (!q.empty()) {
      int current = q.front();
      q.pop();

      for (int neighbor : adj[current]) {
        if (!suspicious[neighbor]) {
          suspicious[neighbor] = true;
          q.push(neighbor);
        }
      }
    }

    bool can_remove = true;
    for (auto &edge : invocations) {
      int caller = edge[0];
      int reciever = edge[1];

      if (!suspicious[caller] && suspicious[reciever]) {
        can_remove = false;
        break;
      }
    }

    vector<int> result;

    if (can_remove) {
      for (int i = 0; i < n; i++) {
        if (!suspicious[i]) {
          result.push_back(i);
        }
      }
    } else {
      for (int i = 0; i < n; i++) {
        result.push_back(i);
      }
    }

    return result;
  };
};

struct TestCase {
  int n;
  int k;
  vector<vector<int>> invocations;
  vector<int> result;
};

int main() {

  vector<TestCase> testCases = {
      {4, 1, {{1, 2}, {0, 1}, {3, 2}}, {0, 1, 2, 4}},
  };

  Solution s;

  for (auto &t : testCases) {
    auto result = s.remainingMethods(t.n, t.k, t.invocations);
    print("Expected: {}, Got: {}\n", t.result, result);
  }

  return 0;
}
