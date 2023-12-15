from typing import List
from collections import defaultdict

class RangeFreqQuery:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.seg = [0] * (4 * self.n)
        self.frequency = defaultdict(int)
        self.build(1, 0, self.n - 1)
        print(self.seg)
    
    def concate(self, dict1, dict2):
        newDict = defaultdict(int)
        for i, val in dict1.items():
            newDict[i] += val

        for i, val in dict2.items():
            newDict[i] += val
        return newDict
    def build(self, p, s, e):
        if s == e:
            self.seg[p] = {self.nums[s]: 1}
            return

        self.build(2 * p, s, (s + e) // 2)
        self.build(2 * p + 1, (s + e) // 2 + 1, e)
        self.seg[p] = self.concate(self.seg[ 2 * p], self.seg[2 * p + 1])


    def query(self, r1: int, r2: int, value: int) -> int:
        tmp = self.query2(1, 0, self.n -1, r1, r2)
        # print(tmp)
        return tmp[value]
    def query2(self, p, s, e, r1, r2):
        if s >= r1 and e <= r2:
            return self.seg[p]
        if s > r2 or e < r1:
            return {}
        return self.concate(self.query2(2 * p, s, (s + e) // 2, r1, r2), 
                            self.query2(2 * p + 1, (s + e) // 2 + 1, e, r1, r2))




nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3]
slv = RangeFreqQuery(nums)
print(slv.query(0, 3, 1))
