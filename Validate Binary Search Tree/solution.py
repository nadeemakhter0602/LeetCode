# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _isValidBST(root, left_boundary, right_boundary):
            if root is None:
                return True
            elif left_boundary < root.val < right_boundary:
                return _isValidBST(root.left, left_boundary, root.val) and _isValidBST(root.right, root.val, right_boundary)
            return False
        return _isValidBST(root, float('-inf'), float('inf'))