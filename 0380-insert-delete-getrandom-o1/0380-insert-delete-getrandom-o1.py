class RandomizedSet:

    def __init__(self):
        self.ans = []
        self.hmap = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.hmap:
            self.ans.append(val)
            index = len(self.ans) - 1 #index of val
            self.hmap[val] = index
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hmap:
            index = self.hmap[val]

            temp = self.ans[-1]
            self.ans[-1] = self.ans[index]
            self.ans[index] = temp

            self.hmap[temp] = index

            self.ans.pop()
            self.hmap.pop(val)

            return True
        
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.ans)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()