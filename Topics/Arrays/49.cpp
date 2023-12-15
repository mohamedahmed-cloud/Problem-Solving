class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        map<string, vector<string>> dict;
        for(auto s: strs)
        {
            string tmp = s;
            sort(s.begin(), s.end());
            dict[s].push_back(tmp);
        }
        for(auto it = dict.begin(); it != dict.end(); it++)
        {
            vector<string> arr;
            for(auto curr: it->second)
                arr.push_back(curr);
            ans.push_back(arr);
        }
        return ans;
    }
};