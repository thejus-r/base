#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, a;
    cin >> n;
    cin >> a;

    int lc = 0, rc = 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x < a) {
            lc++;
        } else if (x > a) {
            rc++;
        }

    }

    if (lc > rc) {
        cout << a - 1;
    } else {
        cout << a + 1;
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
