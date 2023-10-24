class RandomizedSet:

    def __init__(self):
        self.s = dict()

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        else:
            self.s[val] = True
            return True

    def remove(self, val: int) -> bool:
        if val in self.s:
            del self.s[val]
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(list(self.s.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()