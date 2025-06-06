# Last updated: 6/5/2025, 5:40:03 PM
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.nums = []
        
    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.nums.append(val)
            self.map[val] = len(self.nums) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        i = self.map[val]
        temp = self.nums[-1]
        self.nums[-1] = self.nums[i]
        self.nums[i] = temp
        self.map[temp] = i

        self.nums.pop()
        self.map.pop(val)
        return True

        
    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()