from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        indx = self.calendar.bisect_right((start, end))
        if (indx > 0 and self.calendar[indx -1][1] > start)\
            or (indx < len(self.calendar) and end > self.calendar[indx][0]):
            return False
        self.calendar.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)