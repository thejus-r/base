#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    const int INF = 1e9;
    vector<bool> has(n + 1, false);
    vector<int> dp(n + 1, INF);

    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        if (x <= n) {
            has[x] = true;
            dp[x] = 1;
        }
    }

    for (int i = 1; i <= n; i++) {

        if (dp[i] == INF) continue;

        for (int j = 2; i * j <= n; j++) {
            if (has[j]) {
                dp[i * j] = min(dp[i * j], dp[i] + 1);
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        if (dp[i] == INF) {
            cout << -1;
        } else {
            cout << dp[i];
        }

        if (i <= n) {
            cout << ' ';
        }
    }

    cout << '\n';
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
