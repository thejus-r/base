#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    int n, q;
    cin >> n;
    cin >> q;

    vector<ll> a(n + 1, 0);
    vector<ll> b(n, 0);

    for (int i = 0; i < n; i++){
        cin >> a[i];
    }

    for (int i = 0; i < n; i++){
        cin >> b[i];
    }

    for (int i = n - 1; i >= 0; i--) {
        a[i] = max({a[i], a[i + 1], b[i]});
    }

    // prefix sum
    for (int i = 1; i < n; i++) {
        a[i] += a[i - 1];
    }

    for (int i = 0; i < q; i++) {
        int l, r;
        cin >> l;
        cin >> r;

        int d;
        if (l == 1) {
            d = a[r - 1];
        } else {
            d = a[r - 1] - a[l - 2];
        }
        cout << d << ' ';
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
