#include <iostrem>
#include <vector>
#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> dict;
        int n1 = nums.size();
        vector<int> ans;
        for(int i = 0; i < n1; i ++)
        {
            if (dict[nums[i]] != 0)
            {
                ans.push_back(dict[nums[i]] - 1);
                ans.push_back(i);

                return ans;
            }
            dict[target - nums[i]]  = i + 1;
        }
        return ans;

    }
};