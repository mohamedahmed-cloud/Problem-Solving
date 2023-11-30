#include <iostream>
using namespace std;
int main()
{
    long long num, ans, x, y;
    cin >> num;
    ans = 1;
    x=0;
    for (int i = 2; i <= num; i++)
    {
        ans *= i;
    }
    cout<<ans<<endl;
    string s = to_string(ans);
    y = s.length();
    for (int i = 0; i < y; i++)
    {
        x += 1;
    }
    cout << "Number of digits of " << num << "! is " << x << endl;
}