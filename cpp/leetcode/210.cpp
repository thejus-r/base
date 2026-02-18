// 210. Course Schedule II

#include <vector>
#include <print>
#include <queue>
using namespace std;

class Solution {
    public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequistes) {
        vector<vector<int>> adj(numCourses);

        // build adjacency list
        for (auto pre: prerequistes) {
            adj[pre[1]].push_back(pre[0]);
        }

        // find inDegree for the vertex
        vector<int> inDegree(numCourses, 0);

        for (int u = 0; u < numCourses; u++) {
            for (int v: adj[u]) {
                inDegree[v]++;
            }
        }

        // BFS
        queue<int> q;
        for (int i = 0; i < numCourses; i ++) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }

        vector<int> topoSort;
        while (!q.empty()) {
            int u = q.front(); q.pop();

            topoSort.push_back(u);

            for (int v: adj[u]) {
                inDegree[v]--;

                if (inDegree[v] == 0) {
                    q.push(v);
                }
            }

        }

        if (topoSort.size() == numCourses) {
            return topoSort;
        } else {
            return {};
        }
    }
};

struct TestCase {
    int numCourses;
    vector<vector<int>> prerequistes;
    vector<int> expected;
};

int main() {

    vector<TestCase> testCases = {
        { 2, { { 1, 0 } }, { 0, 1 }},
        { 4, { { 1, 0 }, { 2, 0 }, { 3, 1 } }, { 0, 2, 1, 3 }},
    };

    Solution s;
    for (auto t: testCases) {
        vector<int> result = s.findOrder(t.numCourses, t.prerequistes);
        println("{}", result);
    }
    return 0;
}
