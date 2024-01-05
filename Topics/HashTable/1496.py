class Solution:
    def isPathCrossing(self, path: str) -> bool:
        count = set()
        SN = 0
        EW = 0
        count.add((0, 0))
        for i in path:
            if i == "N":
                SN += 1
            elif i == "S":
                SN -= 1
            elif i == "E":
                EW += 1
            elif i == "W":
                EW -= 1
            s = (SN, EW)
            if s in count:
                return True
            count.add(s)
        return False
        