#include <bits/stdc++.h>
using namespace std;

void solve() {
    int x, y;
    cin >> x;
    cin >> y;

    int i = 0;
    while (x <= y) {
        x *= 3;
        y *= 2;
        i++;
    }

    cout << i;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();

    return 0;
}
