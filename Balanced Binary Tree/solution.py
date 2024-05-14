# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            leftLen = 0
            rightLen = 0
            leftLen, isBalancedLeft = dfs(root.left)
            rightLen, isBalancedRight = dfs(root.right)
            treeLen = 1 + max(leftLen, rightLen)
            isBalanced = (
                abs(leftLen - rightLen) <= 1 and isBalancedLeft and isBalancedRight
            )
            return treeLen, isBalanced

        return dfs(root)[1]
