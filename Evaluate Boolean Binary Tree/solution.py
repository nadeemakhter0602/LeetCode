# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        visited = set()
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if curr.val == 2 and curr.left.val <= 1 and curr.right.val <= 1:
                curr.val = curr.left.val == 1 or curr.right.val == 1
            elif curr.val == 3 and curr.left.val <= 1 and curr.right.val <= 1:
                curr.val = curr.left.val == 1 and curr.right.val == 1
            if curr in visited:
                continue
            visited.add(curr)
            stack.append(curr)
            stack.append(curr.left)
            stack.append(curr.right)
        return root.val == 1
