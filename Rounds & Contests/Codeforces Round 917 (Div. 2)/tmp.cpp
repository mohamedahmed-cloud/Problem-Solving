#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

string svalues() {
    string s;
    getline(cin, s);
    return s;
}

int test() {
    int n;
    cin >> n;
    cin.ignore();  
    return n;
}

void dfs(string s, unordered_set<string>& ans) {
    if (ans.find(s) == ans.end()) {
        return;
    }
    ans.insert(s);
    if (s.length() <= 1) {
        return;
    }
    dfs(s.substr(1), ans);
    if (s.length() > 2) {
        dfs(s.substr(0, 1) + s.substr(2), ans);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t = test();
    while (t--) {
        string s = svalues();
        unordered_set<string> ans;
        dfs(s, ans);
        cout << ans.size() << endl;
    }

    return 0;
}
