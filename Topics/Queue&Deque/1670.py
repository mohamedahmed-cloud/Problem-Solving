from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.queue = deque()
        self.n = 0

    def pushFront(self, val: int) -> None:
        self.queue.appendleft(val)
        self.n += 1


    def pushMiddle(self, val: int) -> None:
        self.queue.insert(self.n // 2, val)
        self.n += 1

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        self.n += 1

    def popFront(self) -> int:
        if self.n == 0: return -1
        self.n -= 1
        return self.queue.popleft()


    def popMiddle(self) -> int:
        if self.n == 0: return -1
        self.n -= 1
        tmp = self.queue[self.n // 2]
        del self.queue[self.n // 2]
        return tmp

    def popBack(self) -> int:
        if self.n == 0: return -1
        self.n -= 1
        return self.queue.pop()
