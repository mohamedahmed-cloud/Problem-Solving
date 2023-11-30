#include <iostream>
using namespace std;
int main()
{
    int num, ans, len, y;
    cin >> num;
    ans = 1;
    len=0;
    for (int i = 2; i <= num; i++)
    {
        ans *= i;
    }
    string s = to_string(ans);
    y = s.length();
    for (int i = 0; i < y; i++)
    {
        len += 1;
    }
    cout << "Number of digits of " << num << "! is " << len << endl;
}