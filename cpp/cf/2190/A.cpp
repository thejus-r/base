#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;

    string str;
    cin >> str;

    string sorted_str = str;
    sort(sorted_str.begin(), sorted_str.end());

    int c = 0;
    vector<int> seq;
    for (int i = 0; i < n; i++) {
        if (str[i] != sorted_str[i]) {
            c++;
            seq.push_back(i + 1);
        }
    }

    if (c == 0){
        cout << "Bob" << '\n';
    } else {
        cout << "Alice" << '\n';
        cout << c << '\n';

        for (int x: seq) {
            cout << x << ' ';
        }

        cout << '\n';
    }
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
