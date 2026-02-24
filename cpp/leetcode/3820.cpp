// 3820. Pythagorean Distance Nodes in a Tree

#include <deque>
#include <vector>
#include <print>

using namespace std;
class Solution {
    public:
    int specialNodes(int n, vector<vector<int>>& edges, int x, int y, int z) {

        vector<vector<int>> adj(n);

        for (auto edge: edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        auto bfs = [&](int node) -> vector<int> {
            vector<int> dist(n, -1);
            dist[node] = 0;

            deque<int> q;
            q.push_back(node);

            while (!q.empty()) {
                int u = q.front(); q.pop_front();

                for (int v: adj[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                    }
                }

            }

            return dist;
        };

        vector<int> dx = bfs(x), dy = bfs(y), dz = bfs(z);

        int result = 0;
        for (int i = 0; i < n; ++i) {
            long long a = dx[i], b = dy[i], c = dz[i];

            if (a > b) { long long t = a; a = b; b = t; }
            if (b > c) { long long t = b; b = c; c = t; }
            if (a > b) { long long t = a; a = b; b = t; }

            result += int(a * a + b * b == c * c);
        }

        return result;
    }
};


struct TestCase {
    int n;
    vector<vector<int>> edges;
    int x;
    int y;
    int z;
    int result;
};

int main() {

    Solution s;

    vector<TestCase> testCases = {
        { 4, { {0, 1}, {0, 2}, {0, 3} }, 1, 2, 3, 3 }
    };

    for (TestCase t: testCases) {
        int result = s.specialNodes(t.n, t.edges, t.x, t.y, t.z);
        println("Expected: {}, Got: {}", t.result, result);
    }

    return 0;
}
