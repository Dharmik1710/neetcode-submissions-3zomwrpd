class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = 2**31

    def push(self, val: int) -> None:
        self.min_ = min(self.min_, val)
        self.stack.append((val, self.min_))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        if self.stack:
            self.min_ = self.stack[-1][1]
        else:
            self.min_ = 2**31

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_