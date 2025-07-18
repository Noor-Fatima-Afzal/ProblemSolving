# Problem Link: https://leetcode.com/problems/diameter-of-binary-tree/
#
# Problem:
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes.
# The path may or may not pass through the root.

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = []
    node_to_depth = {}
    diameter = 0

    stack.append(root)

    while stack:
        node = stack[-1]

        if node.left and node.left not in node_to_depth:
            stack.append(node.left)
        elif node.right and node.right not in node_to_depth:
            stack.append(node.right)
        else:
            stack.pop()
            left_depth = node_to_depth.get(node.left, 0)
            right_depth = node_to_depth.get(node.right, 0)

            node_to_depth[node] = 1 + max(left_depth, right_depth)

            diameter = max(diameter, left_depth + right_depth)

    return diameter
