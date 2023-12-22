class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int length = flowerbed.size();
        int cnt = 0;
        for (int i = 0; i < length; i++) {
            bool left = (i == 0 || flowerbed[i - 1] == 0);
            bool right = (i + 1 == length  || flowerbed[i + 1] == 0);
            if (left && right && flowerbed[i] == 0)
            {
                flowerbed[i] = 1;
                cnt += 1;

            }

        }
        return cnt >= n;
    }
};