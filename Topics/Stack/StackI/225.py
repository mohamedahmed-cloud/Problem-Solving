class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        # print(self.q1)
        prev = 0
        while self.q1:
            if prev:
                self.q2.append(prev)

            prev = self.q1.pop(0)
        
        while  self.q2:
            self.q1.append(self.q2.pop(0))
        print(self.q1)
        return prev

    def top(self) -> int:
        prev = 0
        while self.q1:
            prev = self.q1.pop(0)
            self.q2.append(prev)

        
        while  self.q2:
            self.q1.append(self.q2.pop(0))

        return prev

    def empty(self) -> bool:
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()