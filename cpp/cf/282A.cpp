#include <cstring>
#include <iostream>
#include <string>
using namespace std;

int main() {
    std::ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int x = 0;
    string s;
    while (n--){
        cin >> s;

        if (s[1] == '+') {
            x++;
        } else {
            x--;
        }
    }

    cout << x << endl;

    return 0;
}
