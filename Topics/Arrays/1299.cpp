class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int mx = -1;
        int size = arr.size();

        for (int i = size - 1; i >= 0; i --)
        {
            int tmp = arr[i];
            arr[i] = mx;
            mx = max(tmp, mx);
        }
        return arr;
    }
};