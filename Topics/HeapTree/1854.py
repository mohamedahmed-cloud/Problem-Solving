from heapq import heapify, heappop, heappush

class SeatManager:

    def __init__(self, n: int):
        self.heap = [i + 1 for i in range(n)]
        heapify(self.heap)

    def reserve(self) -> int:
        return heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
