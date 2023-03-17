# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root, res):
            if root is None:
                return
            res.append(root.val)
            preorder(root.left, res)
            preorder(root.right, res)
        res = []
        preorder(root, res)
        return res

    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []
        curr = root
        while curr is not None and len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return res