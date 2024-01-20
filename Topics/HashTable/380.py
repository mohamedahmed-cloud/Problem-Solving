from collections import defaultdict
from random import choice
class RandomizedSet:

    def __init__(self):
        self.data = defaultdict(int)
        self.lst = []
        self.n = 1

    def insert(self, val: int) -> bool:
        if self.data[val] == 0:
            self.data[val] = self.n
            self.lst.append(val)
            self.n += 1
            return True
        return False


    def remove(self, val: int) -> bool:
        if self.data[val] == 0: return False

        indx = self.data[val] - 1
        self.lst[indx] = self.lst[-1]
        self.data[self.lst[-1]]= indx + 1
        # print("berfore", self.lst)
        self.lst.pop()
        # print("after", self.lst)
        self.data[val] = 0
        self.n -= 1
        return True

    def getRandom(self) -> int:
        # print(self.lst, self.data)
        return choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(0)
param_2 = obj.insert(1)
param_3 = obj.remove(0)
param_2 = obj.insert(2)
param_3 = obj.remove(1)
print(obj.getRandom())
print(param_1, param_2, param_3)
