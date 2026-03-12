#include <bits/stdc++.h>
#include <vector>
using namespace std;

typedef long long ll;

void solve() {
    int n;
    cin >> n;

    vector<ll> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }

    sort(a.rbegin(), a.rend());

    vector<ll> b(n);
    for (int i = 0; i < n; i++){
        cin >> b[i];
    }

    ll max_score = 0;

    ll current_needed_swords = 0;

    // iterate through levels
    for (long long k = 1; k <= n; k++) {
        current_needed_swords += b[k - 1];

        if (current_needed_swords > n) {
            break;
        }

        ll current_difficulty = a[current_needed_swords - 1];
        ll current_score = k * current_difficulty;
        max_score = max(max_score, current_score);
    }

    cout << max_score << '\n';

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
