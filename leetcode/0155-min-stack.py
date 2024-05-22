class MinStack:

    def __init__(self):
        self.min_val = []
        self.entry = []

    def push(self, val: int) -> None:
        if not self.min_val:
            self.min_val.append(val)
        else:
            self.min_val.append(min(self.min_val[-1], val))
        self.entry.append(val)

    def pop(self) -> None:
        self.entry.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.entry[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
