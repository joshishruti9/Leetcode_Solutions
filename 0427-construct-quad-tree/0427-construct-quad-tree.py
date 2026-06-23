"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def merge(self, upper_left, upper_right, lower_left, lower_right):
        isLeaf = False

        if upper_left.val == upper_right.val == lower_left.val == lower_right.val and (upper_left.isLeaf == lower_left.isLeaf == upper_right.isLeaf == lower_right.isLeaf == True):
            isLeaf = True
            node = Node(upper_left.val, isLeaf, None, None, None, None)
        else:
            node = Node(upper_left.val, isLeaf, upper_left, upper_right, lower_left, lower_right)

        return node


    def break_quad(self, grid, start_row, end_row, start_col, end_col):

        if start_row == end_row and start_col == end_col:
            node = Node(grid[start_row][start_col], True, None, None, None, None)
            return node

        if start_row != end_row and start_col != end_col:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2

            upper_left = self.break_quad(grid, start_row, mid_row, start_col, mid_col)
            lower_left = self.break_quad(grid, mid_row+1, end_row, start_col, mid_col)
            upper_right = self.break_quad(grid, start_row, mid_row, mid_col+1, end_col)
            lower_right = self.break_quad(grid, mid_row+1, end_row, mid_col+1, end_col)

            node = self.merge(upper_left, upper_right, lower_left, lower_right)
            return node

    def construct(self, grid: List[List[int]]) -> 'Node':
        start_row = 0
        end_row = len(grid) - 1

        start_col = 0
        end_col = len(grid[0]) - 1

        node = self.break_quad(grid, start_row, end_row, start_col, end_col)
        return node