from random import choice

class RandomizedSet:

    def __init__(self):
        self.indices = dict()
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.nums.append(val)
            self.indices[val] = len(self.nums) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.indices:
            index = self.indices[val]
            self.indices[self.nums[-1]] = index
            self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
            self.nums.pop()
            self.indices.pop(val)
            return True

        return False

    def getRandom(self) -> int:
        return choice(self.nums)
