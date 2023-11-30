from collections import deque

class RecentCounter:

    def __init__(self):
        self.counter = deque()
        self.cnt = 0

    def ping(self, t: int) -> int:
        self.counter.append(t)
        self.cnt += 1
        while self.counter[-1] - 300 > self.counter[0]:
             self.cnt -= 1
             self.counter.popleft()
        return self.cnt


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)