#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    vector<int> nums(n);

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int zero_count = 0, one_count = 0;
    for (int x: nums) {
        if (x == 0) {
            zero_count++;
        } else if (x == 1) {
            one_count++;
        }
    }

    string res = "NO";

    if (zero_count == 0) {
        res = "NO";
    } else if (zero_count == 1) {
        res = "YES";
    } else if (zero_count >= 2 && one_count == 0) {
        res = "NO";
    } else if (zero_count >= 2 && one_count >= 1) {
        res = "YES";
    }

    cout << res << '\n';
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
