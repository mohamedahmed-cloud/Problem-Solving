class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> mapTwoVector;
        vector<int> stack;
        int n = nums2.size();

        for (int i = 0; i < n; i++) {
            while(!stack.empty() && nums2[i] > stack[stack.size() - 1]) {
                mapTwoVector[stack.back()] = nums2[i];
                stack.pop_back();
            }
            stack.push_back(nums2[i]);
        }
        int idx = 0;
        for (auto num: nums1) {
            int tmp = mapTwoVector[num];
            tmp ? nums1[idx] = tmp: nums1[idx] = -1 ;
            idx++;
        }
        return nums1;
    }
};