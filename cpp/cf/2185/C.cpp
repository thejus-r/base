#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> nums(n);

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    sort(nums.begin(), nums.end());

    int max_streak = 1;
    int curr_streak = 1;

    for (int i = 1; i < n; i++) {
        if (nums[i - 1] + 1 == nums[i]) {
            curr_streak ++;
            max_streak = max(max_streak, curr_streak);
        } else if (nums[i - 1] == nums[i]) {
            continue;
        } else {
            curr_streak = 1;
        }
    }

    cout << max_streak << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}
