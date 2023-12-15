from collections import deque

class MyCalendarTwo:

    def __init__(self):
        self.calendar = deque()
        self.overlap = deque()

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlap:
            if end > s and start < e:
                return False
        for s, e in self.calendar:
            if end > s and start < e:
                self.overlap.append((max(s, start), min(e, end)))
        self.calendar.append((start, end))
        # print(self.calendar, self.overlap)
        return True
        



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)