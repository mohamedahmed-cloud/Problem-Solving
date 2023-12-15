class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, char> count1;
        map<char, char> count2;

        for(int i = 0; i < s.size(); i++)
        {
            if ( (count1[s[i]] && count1[s[i]] != t[i]) ||
                 (count2[t[i]] && count2[t[i]] != s[i]) ) return false;
            count1[s[i]] = t[i];
            count2[t[i]] = s[i];
        }
        return true;
    }
};