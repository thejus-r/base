#include <ios>
#include <iostream>
#include <string>

using namespace std;

int main() {
    std::ios_base::sync_with_stdio(false);
    int n;

    if (cin >> n) {
        while (n--) {
            string s;
            cin >> s;

            int l = s.length();

            if (l > 10) {
                string ns;
                ns += s[0];
                ns += to_string(l - 2);
                ns += s[l - 1];
                cout << ns << '\n';
            } else {
                cout << s << '\n';
            }
        }
    }
}
