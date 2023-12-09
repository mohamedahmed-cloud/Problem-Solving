from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg = [0] * (4 * self.n)
        def build(p = 1, s = 0, e = self.n -1):
            if s == e:
                self.seg[p] = nums[s]
                return 
            build(2 * p, s, (s + e) // 2)
            build(2 * p + 1,(s + e) // 2 + 1, e)
            self.seg[p] = self.seg[2 * p] + self.seg[2 * p + 1]
        build()
        # print(self.seg, nums)

    def update(self, index: int, val: int) -> None:
        def update(index, val, p = 1, s = 0, e = self.n -1):
            if s == e:
                self.seg[p] = val
                return
            if index <= (s + e) // 2:
                update(index, val, 2 * p, s, (s + e) // 2)
            else:
                update(index, val, 2 * p + 1, (s + e) // 2 + 1, e)
            self.seg[p] = self.seg[2 * p] + self.seg[2 * p + 1]
        update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        def get(r1, r2, p = 1, s = 0 , e = self.n -1):
            if s >= r1 and e <= r2:
                return self.seg[p]
            if s > r2 or e < r1:
                return 0
            return get(r1, r2, 2 * p, s, (s + e) // 2) + get(r1, r2, 2 * p + 1, (s + e) // 2 + 1, e)
        return get(left, right)

# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
# obj.update(index,val)
param_2 = obj.sumRange(0, 2)
print(param_2)