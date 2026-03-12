#include <bits/stdc++.h>
using namespace std;

void solve() {
    vector<vector<int>> matrix(5, vector<int>(5));
    int input;
    int targetRow = 0, targetCol = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> input;
            if (input == 1) {
                targetCol = j;
                targetRow = i;
            }
        }
    }

    int d = abs(targetRow - 2) + abs(targetCol - 2);
    cout << d;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}
