class Solution {
public:
    int lengthOfLastWord(string s) {
        int cnt = 0;
        int last = 0;
        for (auto ch: s)
        {
            if (ch == ' ')
            {
                if (cnt != 0)
                last = cnt;
                cnt = 0;
            }
            else {
                cnt ++;
            }
        }
        cout << last;
        if (cnt != 0) return cnt;
        return last;
    }
};