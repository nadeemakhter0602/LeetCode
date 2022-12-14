# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post_order(root, res):
            if root is None:
                return
            post_order(root.left, res)
            post_order(root.right, res)
            res.append(root.val)
        res = []
        post_order(root, res)
        return res

    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []
        while len(stack) > 0 and root is not None:
            curr = stack.pop()
            res.append(curr.val)
            if curr.left is not None:
                stack.append(curr.left)
            if curr.right is not None:
                stack.append(curr.right)
        return res[::-1]