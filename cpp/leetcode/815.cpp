// 815. Bus Routes

#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <print>
#include <cassert>

using namespace std;

class Solution {
    public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) return 0;

        unordered_map<int, vector<int>> adjList;

        for (int route = 0; route < routes.size(); route ++) {
            for (int stop: routes[route]) {
                adjList[stop].push_back(route);
            }
        }

        queue<int> q;
        unordered_set<int> vis;

        for (auto route: adjList[source]) {
            q.push(route);
            vis.insert(route);
        }

        int busCount = 1;
        while (!q.empty()) {
            int size = q.size();

            for (int i = 0; i < size; i ++) {
                int route = q.front(); q.pop();

                for (auto stop: routes[route])  {
                    if (stop == target) {
                        return busCount;
                    }

                    for (auto nextRoute: adjList[stop]) {
                        if (!vis.count(nextRoute))  {
                            vis.insert(nextRoute);
                            q.push(nextRoute);
                        }
                    }
                }
            }

            busCount++;

        }
        return -1;
    }
};

struct TestCase {
  vector<vector<int>> routes;
  int source, target, expected;
};

int main(){

    vector<TestCase> testCases =  {
        { { { 1, 2, 7 }, { 3, 6, 7 } }, 1, 6, 2 },
        { { { 7, 12 }, { 4, 5, 15 }, { 6 }, { 15, 19 }, { 9, 12, 13 } }, 15, 12, -1 },
    };

    Solution s;

    for (auto t: testCases) {
        int result = s.numBusesToDestination(t.routes, t.source, t.target);
        println("Expected: {}, Got: {}.", t.expected, result);
        assert(result == t.expected);
    }

    return 0;
}
