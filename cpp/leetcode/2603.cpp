// 2603. Collect Coins in a Tree

#include <queue>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    int collectTheCoins(vector<int>& coins, vector<vector<int>>& edges) {
        int n = coins.size(); // no. of nodes
        vector<vector<int>> adj(n, vector<int>{});
        vector<bool> active(n, true);

        // build undirected adj list from the edges
        // Calculate Degree to find leaf nodes

        vector<int> degree(n, 0);

        for (auto edge: edges) {
            int u = edge[0], v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
            degree[u]++;
            degree[v]++;
        }

        queue<int> q;

        for (int i = 0; i < n; i++) {
            if (degree[i] == 1 && coins[i] != 1) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int u = q.front(); q.pop();

            for(auto v: adj[u]) {
                degree[v]--;

                if (degree[v] == 1 && coins[v] == 0) {
                    q.push(v);
                }
            }
            active[u] = false;
            degree[u] = 0;
        }

        for (int i = 0; i < n; i++) {
            if (coins[i] == 1 && degree[i] == 1) {
                q.push(i);
            }
        }

        int layer = 0;
        while (!q.empty() && layer < 2) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                int u = q.front(); q.pop();

                for (auto v: adj[u]) {
                    if (degree[v] > 1) {
                        degree[v]--;
                    }

                    if (degree[v] == 1) {
                        q.push(v);
                    }
                }

                active[u] = false;
                degree[u] = 0;
            }

            layer++;
        }

        int remainingNode = 0;
        for (bool node: active) {
            if (node) remainingNode++;
        }

        if (!remainingNode) {
            return 0;
        } else {
            return (remainingNode - 1) * 2;
        }
    }
};

struct TestCase {
    vector<int> coins;
    vector<vector<int>> edges;
    int result;
};

int main() {

    Solution s;

    vector<TestCase> testCases = {
        { { 1, 0, 0, 0, 0, 1 }, { { 0, 1 }, { 1, 2 }, { 2, 3 }, { 3, 4 }, { 4, 5 } }, 2 },
        { { 0, 0, 0, 1, 1, 0, 0, 1 }, { { 0, 1 }, { 0, 2 }, { 1, 3 }, { 1, 4 }, { 2, 5 }, { 5, 6 }, { 5, 7 } }, 2 },
        { { 0, 1 }, { { 0, 1 } }, 0 },
        { { 0, 0 }, { { 0, 1 } }, 0 },
        { { 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0 }, { { 0, 1 }, { 1, 2 }, { 1, 3 }, { 2, 4 }, { 4, 5 }, { 5, 6 }, { 5, 7 }, { 4, 8 }, { 7, 9 }, { 7, 10 }, { 10, 11 } }, 4 },
        { { 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1 }, { { 0, 1 }, { 1, 2 }, { 2, 3 }, { 2, 4 }, { 2, 5 }, { 2, 6 }, { 4, 7 }, { 6, 8 }, { 5, 9 }, { 4, 10 }, { 6, 11 } }, 0 },
    };

    for (TestCase t: testCases) {
        int result = s.collectTheCoins(t.coins, t.edges);
        println("Expected: {}, Got: {}", t.result, result);
    }
    return 0;
}
