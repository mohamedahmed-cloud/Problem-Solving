from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.hash = defaultdict(list)
        n = len(arr)
        for i in range(n):
            self.hash[arr[i]].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        l = bisect_left(self.hash[value], left)
        r = bisect_right(self.hash[value], right)
        return r - l



nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3]
slv = RangeFreqQuery(nums)
print(slv.query(0, 3, 1))
