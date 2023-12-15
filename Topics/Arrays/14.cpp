class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        int n2 = strs[0].size();
        int mx = 0;
        string ans="";

        for(int i = 0; i < n2; i++)
        {
            for(int j = 1; j < n; j++)
            {
                if (strs[j][i] != strs[j - 1][i])
                {
                    int cnt = 0;
                    for(auto ch: strs[0])
                    {
                        if (cnt == mx) break;
                        ans += (ch);
                        cnt++;
                    }
                    return ans;
                }
            }
            mx += 1;

        }
        return strs[0];

    }
};