// 3871. Count Commas in Range II

#include <vector>
#include <utility>
#include <algorithm>
#include <unordered_map>
#include <print>

using namespace std;

class UnionFind {
  public:
  vector<int> parent;
  vector<int> size; // stores size of parent node

  // init
  UnionFind(int n) {
    parent.resize(n);
    size.resize(n, 1);

    // set parent of each as itself
    for (int i = 0; i < n; i++) {
      parent[i] = i;
    }
  }

  int uFind(int x) {
    if (parent[x] == x) {
      return x;
    }

    return parent[x] = uFind(parent[x]);
  }

  void uUnion(int a, int b) {
    int root_a = uFind(a);
    int root_b = uFind(b);

    if (root_a != root_b) {
      // we check the sizes
      // always keep root_a bigger
      if (size[root_a] < size[root_b]) {
        swap(root_a, root_b);
      }

      parent[root_b] = root_a;

      // update size of root_a
      size[root_a] += size[root_b];
    }
  }

};

class Solution {
  public:
    int maxActivated(vector<vector<int>> &points) {
      int n = points.size();

      UnionFind uf(n);

      unordered_map<int, int> x_map;
      unordered_map<int, int> y_map;

      // populate connected components
      // compress the coordination 0 - n index

      for (int i = 0; i < n; i++) {
        int x = points[i][0];
        int y = points[i][1];

        if (x_map.find(x) != x_map.end()) {
          // already present, we have to connect
          uf.uUnion(i, x_map[x]);
        } else {
          x_map[x] = i;
        }


        if (y_map.find(y) != y_map.end()) {
          // already present, we have to connect
          uf.uUnion(i, y_map[y]);
        } else {
          y_map[y] = i;
        }
      }

      vector<int> component_sizes;

      for (int i = 0; i < n; i++) {
        if (uf.parent[i] == i) {
          component_sizes.push_back(uf.size[i]);
        }
      }

      sort(component_sizes.rbegin(), component_sizes.rend());

      if (component_sizes.size() >= 2) {
        return component_sizes[0] + component_sizes[1] + 1;
      } else {
        return component_sizes[0] + 1;
      }
    }
};

struct TestCase {
  vector<vector<int>> points;
  int result;
};

int main() {
  vector<TestCase> testCases = {
    { { { 1, 1 }, { 1, 2 }, { 2, 2 } }, 4 },
  };

  Solution s;

  for (TestCase t: testCases) {
    auto result = s.maxActivated(t.points);
    println("Expected: {}, Got: {}", t.result, result);
  }

}
