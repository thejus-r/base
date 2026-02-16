// 721. Accounts Merge

#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
    private:
    unordered_set<string> visited;
    unordered_map<string, vector<string>> adjacent;

    void DFS(vector<string>& mergedAccount, string& email) {
        visited.insert(email);
        mergedAccount.push_back(email);

        for (auto neighbor: adjacent[email]) {
            if (visited.find(neighbor) != visited.end()) {
                DFS(mergedAccount, neighbor);
            }
        }
    }

    public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        for (auto account: accounts) {
            int accountSize = account.size();
            string firstEmail = account[1];

            for (int j = 2; j < accountSize; j++) {
                adjacent[firstEmail].push_back(account[j]);
                adjacent[account[j]].push_back(firstEmail);
            }
        }

        vector<vector<string>> mergedAccounts;

        for (auto account: accounts) {
            string accountName = account[0];
            string accountFirstEmail = account[1];

            if (visited.find(accountFirstEmail) != visited.end()) {
                vector<string> mergedAccount;
                DFS(mergedAccount, accountFirstEmail);

                sort(mergedAccount.begin() + 1, mergedAccount.end());
                mergedAccounts.push_back(mergedAccount);
            }
        }
        return mergedAccounts;
    }
};
