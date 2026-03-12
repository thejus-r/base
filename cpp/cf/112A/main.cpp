#include <bits/stdc++.h>
#include <cctype>
using namespace std;

void solve() {
    string s1;
    string s2;

    cin >> s1;
    cin >> s2;

    int res = 0;

    int n = s1.size();
    for (int i = 0; i < n; i++) {
        int c1 = (int)tolower(s1[i]);
        int c2 = (int)tolower(s2[i]);

        if (c1 > c2) {
            res = 1;
            break;
        } else if (c1 < c2) {
            res = -1;
            break;
        }
    }

    cout << res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();

    return 0;
}
