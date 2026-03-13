#include <bits/stdc++.h>
using namespace std;

void solve() {
    string s;
    cin >> s;
    int n = s.length();

    int ops = 0;
    // check edges
    if (s[0] == 'u') {
        s[0] = 's';
        ops++;
    }

    if (s[n - 1] == 'u') {
        s[n - 1] = 's';
        ops++;
    }

    // inner part
    for (int i = 1; i <= n - 2; i++) {
        if (s[i] == 'u' && s[i - 1] == 'u') {
            s[i] = 's';
            ops++;
        }
    }

    cout << ops << '\n';
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
