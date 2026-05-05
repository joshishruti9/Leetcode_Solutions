# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def traverse(self, node):
        if node.left is None and node.right is None:
            self.stack.append(node.val)
            return

        if node.left:
            self.traverse(node.left)
        self.stack.append(node.val)
        if node.right:
            self.traverse(node.right)


    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.traverse(root)
        self.size = len(self.stack)
        self.curr_index = 0

    def next(self) -> int:
        num = self.stack[self.curr_index]
        self.curr_index += 1
        return num

        

    def hasNext(self) -> bool:
        if self.curr_index < self.size:
            return True
        
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()