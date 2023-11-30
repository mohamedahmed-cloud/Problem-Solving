#!/usr/bin/env python3
from heapq import heapify, heappop, heappush
class SeatManager:

    def __init__(self, n: int):
        self.n = n
        self.seates =[i for i in range(1, n + 1)]
        heapify(self.seates)

    def reserve(self) -> int:
        return heappop(self.seates)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seates, seatNumber)


