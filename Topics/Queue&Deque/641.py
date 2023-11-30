from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = deque()
        self.k = k
        self.cnt = 0

    def insertFront(self, value: int) -> bool:
        if self.cnt < self.k:
            self.deque.appendleft(value)
            self.cnt += 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.cnt < self.k:
            self.deque.append(value)
            self.cnt += 1
            return True
            
    def deleteFront(self) -> bool:
        if self.cnt > 0:
            self.deque.popleft()
            self.cnt -= 1
            return True

    def deleteLast(self) -> bool:
        if self.cnt > 0:
            self.deque.pop()
            self.cnt -= 1
            return True

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]
        return -1

    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]
        return -1

    def isEmpty(self) -> bool:
        return True if not self.deque else False 

    def isFull(self) -> bool:
        return len(self.deque) == self.k

