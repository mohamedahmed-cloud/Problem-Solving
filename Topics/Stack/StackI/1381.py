class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize
        self.top = 0

    def push(self, x: int) -> None:
        if self.top < self.size:
            self.stack.append(x)
            self.top += 1

    def pop(self) -> int:
        self.top = max(0, self.top - 1)
        if self.stack: return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:

        times = min(k , len(self.stack))

        for i in range(times):
            self.stack[i] += val

           
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)