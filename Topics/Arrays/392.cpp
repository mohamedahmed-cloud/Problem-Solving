class Solution {
public:
    bool isSubsequence(string s, string t) {
        int n1 = s.size();
        int n2 = t.size();

        int cnt = 0;
        for(int i = 0; i < n2; i++)
        {
            if (s[cnt] == t[i])
            {
                cnt += 1;
            }
        }
        return cnt == n1;
    }
};