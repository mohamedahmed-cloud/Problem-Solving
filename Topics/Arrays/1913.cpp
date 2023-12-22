class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        int mx = 0;
        int mx2 = 0;
        int mn = 10000;
        int mn2 = 10000;
        for (auto num: nums)
        {
            if (num > mx) {
                mx2 = mx;
                mx = num;
            }
            else if (num > mx2) mx2 = num;
            if (num < mn) {
                mn2 = mn;
                mn = num; 
            }
            else if (num < mn2) mn2 = num;
        }
        // cout << mx << mx2 << mn<<mn2;
        return (mx * mx2 - mn * mn2);
    }
};