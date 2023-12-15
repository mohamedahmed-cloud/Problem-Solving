class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> map1;
        for(auto ch: s)
        {
            map1[ch] += 1;
        }
        for(auto ch: t)
        {
            map1[ch] -= 1;
            if(map1[ch] < 0)
            return false;
        }
        for(auto ch: s)
        {
            if(map1[ch] > 0)
            return false;
        }
        return true;
    }
};