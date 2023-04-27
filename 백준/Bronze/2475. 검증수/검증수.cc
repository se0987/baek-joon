#include <iostream>
using namespace std;

int main() {
    int a, b, c, d, e, ans;
    cin >> a >> b >> c >> d >> e;

    ans = (a*a + b*b + c*c + d*d + e*e)%10;

    cout << ans;

    return 0;
}