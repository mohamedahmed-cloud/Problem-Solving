class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        map<string, int> count;
        for(auto city: paths)
        {
            count[city[0]] -= 1;
            count[city[1]] += 1;
        }
        for(auto it = count.begin(); it != count.end(); it++)
        {
            if(it->second == 1) return it->first;
            cout<<it->first<<it->second;
        }
        return "";
    }
};