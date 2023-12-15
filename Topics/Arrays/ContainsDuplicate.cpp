#include <iostream>
#include <map>
#include <vector>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> arr;
        for(int i = 0; i < nums.size(); i++){
            arr[nums[i]] += 1;
            if (arr[nums[i]] >= 2)
                return true;
            
        }

        return false;
    }
};