from collections import deque
class Node:
    def __init__(self, key = 0, val = 0, prev_node = None, next_node = None):
        self.key = key
        self.val = val
        self.prev = prev_node
        self.next = next_node

class LRUCache:

    def __init__(self, capacity: int):

        self.dict = {}
        self.cap = capacity
        self.lrupseudo = Node()
        self.mrupseudo = Node()

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        node = self.dict[key]

        prev_node = node.prev
        next_node = node.next

        prev_node.next = node.next
        next_node.prev = node.prev

        mru_node = self.mrupseudo.prev

        node.prev = mru_node
        self.mrupseudo.prev = node
        node.next = self.mrupseudo
        mru_node.next = node
        print(self)
        return node.val        

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if len(self.dict) == 0:
                new_node = Node(key, value)
                self.lrupseudo.next = new_node
                self.mrupseudo.prev =  new_node
                new_node.prev = self.lrupseudo
                new_node.next = self.mrupseudo
                self.dict[key] = new_node

            elif len(self.dict) < self.cap:
                new_node = Node(key, value)
                mru_node = self.mrupseudo.prev
                new_node.prev = mru_node
                mru_node.next = new_node
                new_node.next = self.mrupseudo
                self.mrupseudo.prev = new_node
                self.dict[key] = new_node

            else:
                lru_node = self.lrupseudo.next
                
                self.dict.pop(lru_node.key)
                self.lrupseudo.next = lru_node.next
                lru_node.next.prev =  self.lrupseudo

                new_node = Node(key, value)
                mru_node = self.mrupseudo.prev

                new_node.prev = mru_node
                mru_node.next = new_node
                self.mrupseudo.prev = new_node
                new_node.next = self.mrupseudo                
                self.dict[key] = new_node        
        else:
            node = self.dict[key]

            prev_node = node.prev
            next_node = node.next

            prev_node.next = node.next
            next_node.prev = node.prev

            new_node = Node(key, value)

            mru_node = self.mrupseudo.prev
            new_node.prev = mru_node
            mru_node.next = new_node
            new_node.next = self.mrupseudo
            self.mrupseudo.prev = new_node
            self.dict[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)