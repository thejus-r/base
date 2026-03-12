#include <bits/stdc++.h>
using namespace std;

void solve() {
    string s;
    cin >> s;

    vector<int> nums;

    for (int i = 0; i < s.length(); i += 2){
        nums.push_back(s[i] - '0');
    }

    sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size(); i++ ){
        cout << nums[i];

        if (i < nums.size() - 1) {
            cout << "+";
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();

    return 0;
}
