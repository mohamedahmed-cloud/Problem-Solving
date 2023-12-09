from collections import deque

class MyCalendarTwo:

    def __init__(self):
        self.calendar = deque()

    def book(self, start: int, end: int) -> bool:
        cnt = 0
        for val in self.calendar:
            if val[0] > start or val[1] < end:
                cnt += 1
                if cnt >= 2:
                    return False
            self.calendar.append(val)
            # print(cnt)
            return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)