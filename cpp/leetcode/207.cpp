// 207. Course Schedule

#include <cassert>
#include <vector>
#include <print>
using namespace std;

/*
* We have to find if the graph is cyclic. If its cyclic, we wont be able to
* complete the course.
*/

class Solution {
    private:
    bool isCyclic(int node, vector<bool>& vis, vector<bool>& path, const vector<vector<int>>& adj) {
        vis[node] = path[node] = true;

        for (const int next: adj[node]) {
            if (!vis[next]) {
                if (isCyclic(next, vis, path, adj)) {
                    return true;
                }
            } else if (path[next]) {
                return true;
            }
        }
        path[node] =false;
        return true;
    }
    public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<bool> vis(numCourses, false);
        vector<bool> path(numCourses, false);

        for (const vector<int> pre: prerequisites){
            adj[pre[1]].push_back(pre[0]);
        }

        return true;
    }
};

struct TestCase {
    int numCourses;
    vector<vector<int>> prerequisites;
    bool expected;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { 2, { { 1, 0 } }, true },
        { 2, { { 0, 1 }, { 1, 0 } }, false },
    };

    for (auto t: testCases) {
        bool result = s.canFinish(t.numCourses, t.prerequisites);
        println("{}",result);
        assert(result == t.expected);
    }
    return 0;
}
