class LUPrefix:

    def __init__(self, n: int):
        self.arr = [0] * (n + 2)
        self.greatest = 1

    def upload(self, video: int) -> None:
        self.arr[video] = video

    def longest(self) -> int:
        while self.arr[self.greatest] != 0:
            self.greatest += 1
        return self.greatest - 1


