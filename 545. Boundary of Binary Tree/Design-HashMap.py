1class MyHashMap:
2
3    def __init__(self):
4        self.map = [None for i in range(10 ** 6 + 1)]
5        
6
7    def put(self, key: int, value: int) -> None:
8        self.map[key] = value
9
10    def get(self, key: int) -> int:
11        if self.map[key] == None:
12            return -1
13        
14        return self.map[key]
15        
16
17    def remove(self, key: int) -> None:
18        if self.map[key] != None:
19            self.map[key] = None
20        
21
22
23# Your MyHashMap object will be instantiated and called as such:
24# obj = MyHashMap()
25# obj.put(key,value)
26# param_2 = obj.get(key)
27# obj.remove(key)