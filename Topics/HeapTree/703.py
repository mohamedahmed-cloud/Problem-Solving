#!/usr/bin/env python3
from typing import Optional, List
from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        nums.sort(reverse=True)
        self.check = True
        if  self.check:
            if k <= len(nums):
                self.k_th_array = nums[:k]
            elif nums:
                add = [-float("inf")] * (k - len(nums)) + nums
                self.k_th_array = add
            else:
                self.k_th_array = []
        self.k = k
        heapify(self.k_th_array)
        

    def add(self, val: int) -> int:
        k = self.k
        k_th_array = self.k_th_array
        kth_largest = -float("inf")
        if k_th_array:
              kth_largest = k_th_array[0]

        if val > kth_largest:
            if k_th_array:
                heappop(k_th_array)

            heappush(k_th_array, val)
            self.check = False
            kth_largest = k_th_array[0]

        return kth_largest

# another good Solution
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        n = len(self.heap)
        while  n > k:
            heappop(self.heap)
            n -= 1


    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        print(self.heap[0])

