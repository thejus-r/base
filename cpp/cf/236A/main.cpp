#include <bits/stdc++.h>
using namespace std;

void solve() {
    string str;
    cin >> str;

    int n = str.length();

    bool d[26] = { false };

    for (int i = 0; i < n; i++){
        int c = (int)str[i] - (int)'a';
        d[c] = true;
    }

    int c= 0;
    for (int i = 0; i < 26; i ++) {
        if (d[i]) {
            c++;
        }
    }

    if (c % 2 == 0) {
        cout << "CHAT WITH HER!";
    } else {
        cout << "IGNORE HIM!";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}
