# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def delete(self, node, parent_node):
        
        is_left_child = parent_node and parent_node.left == node 
            
        if node.left is None and node.right is None:
            new_root = parent_node
            if parent_node:
                if is_left_child:
                    parent_node.left = None
                else:
                    parent_node.right = None

            return new_root

        if node.right:
            new_root = node.right

            temp_node = node.right

            while temp_node.left:
                temp_node = temp_node.left
            
            temp_node.left = node.left
            node.left = None

            if parent_node:
                if is_left_child:
                    parent_node.left = new_root
                else:
                    parent_node.right = new_root
        
            return new_root
            

        if node.left:
            new_root = node.left
            node.left = None

            if parent_node:
                if is_left_child:
                    parent_node.left = new_root
                else:
                    parent_node.right = new_root
            
            return new_root
        
        
    def search(self, node, key):

        if not node:
            return None, None
        
        if node.val == key:
            return node, None

        key_node = pnode = None   

        if key < node.val:
            key_node, pnode = self.search(node.left, key)
        else:
            key_node, pnode = self.search(node.right, key)
        
        if not key_node:
            return None, None
        
        if key_node and not pnode:
            return key_node, node
        else:
            return key_node, pnode
        
        return
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node, parent_node = self.search(root, key)

        if node:
            new_root = self.delete(node, parent_node)
            if node == root:
                return new_root
            else:
                return root
        else:
            return root
        