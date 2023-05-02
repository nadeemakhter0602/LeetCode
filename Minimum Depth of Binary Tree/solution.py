# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        m = float('inf')
        while stack:
            curr = stack.pop()
            distance = curr[1]
            curr = curr[0]
            if curr:
                if curr.left:
                    stack.append((curr.left, distance + 1))
                if curr.right:
                    stack.append((curr.right, distance + 1))
                if not curr.left and not curr.right:
                    m = min(distance, m)
        return m
