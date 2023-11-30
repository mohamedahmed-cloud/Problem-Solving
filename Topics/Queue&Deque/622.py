from collections import deque
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque()
        self.k = k
        self.cnt = 0

    def enQueue(self, value: int) -> bool:
        if self.cnt < self.k:
            self.queue.append(value)
            self.cnt += 1
            return True
        

    def deQueue(self) -> bool:
        if self.cnt > 0:
            self.queue.popleft()
            self.cnt -= 1
            return True

    def Front(self) -> int:
        if self.cnt > 0:
            return self.queue[0]
        return -1
    def Rear(self) -> int:
        if self.cnt > 0:
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return  self.cnt == 0 

    def isFull(self) -> bool:
        return self.cnt == self.k


