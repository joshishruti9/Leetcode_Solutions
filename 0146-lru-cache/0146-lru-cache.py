class Node:
    def __init__(self, key=0, value=0, prev_node=None, next_node=None):
        self.key = key
        self.val = value
        self.prev= prev_node
        self.next = next_node

class LRUCache:

    def __init__(self, capacity: int):
        self.lrunode = Node()
        self.mrunode = Node()

        self.mrunode.next = self.lrunode
        self.lrunode.prev = self.mrunode

        self.cap = capacity
        self.key_val = {}
    
    def add_latestnode(self, node):
        prev_node = node.prev
        next_node = node.next

        node.prev = None
        node.next = None

        prev_node.next = next_node
        next_node.prev = prev_node

        old_mrunode = self.mrunode.next
        node.next = old_mrunode
        old_mrunode.prev = node

        node.prev = self.mrunode
        self.mrunode.next = node

    def get(self, key: int) -> int:

        if key not in self.key_val:
            return -1
        
        node = self.key_val[key]

        if node.prev == self.mrunode:
            return node.val

        self.add_latestnode(node)

        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key not in self.key_val:
            #first node
            if len(self.key_val) == 0:
                node = Node(key, value)

                self.mrunode.next = node
                self.lrunode.prev = node
                
                node.next = self.lrunode
                node.prev = self.mrunode

                self.key_val[key] = node

            else:
                if  len(self.key_val) == self.cap:
                    lru = self.lrunode.prev

                    prevnode = lru.prev
                    prevnode.next = self.lrunode
                    self.lrunode.prev = prevnode
                    
                    self.key_val.pop(lru.key)

                newnode = Node(key, value)
                node = self.mrunode.next
                
                node.prev = newnode
                newnode.next = node
                self.mrunode.next = newnode
                newnode.prev = self.mrunode
                self.key_val[key] = newnode

        else:
            node = self.key_val[key]
            node.val = value

            self.add_latestnode(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)