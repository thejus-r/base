#include <ios>
#include <iostream>
using namespace std;

int main() {
    std::ios_base::sync_with_stdio(false);
    int n; cin >> n;
    if (n % 2 == 0 & n > 2) cout << "YES\n";
    else cout << "NO\n";

    return 0;
}
