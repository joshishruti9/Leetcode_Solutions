"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hmap = {}

        fake_head = Node(-1)
        prev_node = fake_head
        node = head

        while node:
            new_node = Node(node.val)
            hmap[node] = new_node
            prev_node.next = new_node
            prev_node = new_node
            node = node.next
        

        node = head

        while node:
            curr_node = hmap[node]
            next_random_node = node.random
            if next_random_node:
                curr_node.random = hmap[next_random_node]
            node = node.next
        
        return fake_head.next