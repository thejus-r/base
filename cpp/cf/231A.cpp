#include <iostream>
using namespace std;

int main() {
    // std::ios_base::sync_with_stdio(false);

    int wins = 0;
    int n;
    if (cin >> n){
        while (n--){
            int cnt = 0;
            for (int i = 0; i < 3; i ++) {
                char c; cin >> c;
                if (c == '1') {
                    cnt += 1;
                }
            }

            if (cnt > 1) {
                wins += 1;
            }
        }
    }
    cout << wins << '\n';
}
