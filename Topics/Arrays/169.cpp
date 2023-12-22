class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cnt = 1;
        int n = nums.size();
        int ans = 0;
        for (auto num: nums)
        {
            if (ans == num)cnt++;
            else cnt--;

            if (cnt == 0) {
                ans = num;
                cnt = 1;
            }
        }
        return ans;
    }
};