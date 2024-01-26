from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []

        for i in ops:
            if i == "+":
                if record[-1] and record[-2]:
                    record.append(record[-1] + record[-2])
                elif record[-1]:
                    record.append(record[-1])
                else:
                    record.append(0)
            elif i == "D":
                record.append(2 * record[-1])
            elif i == "C":
                record.pop()
            else:
                record.append(int(i))
        print(record)
        return sum(record) 