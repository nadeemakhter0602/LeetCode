# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        elif root.left and not root.right:
            return False
        elif not root.left and root.right:
            return False
        elif root.right.val != root.left.val:
            return False
        stack1 = [root.left]
        stack2 = [root.right]
        while stack1 and stack2:
            curr1 = stack1.pop()
            curr2 = stack2.pop()
            if curr1 and curr2:
                if curr1.val == curr2.val:
                    stack1.append(curr1.right)
                    stack1.append(curr1.left)
                    stack2.append(curr2.left)
                    stack2.append(curr2.right)
                else:
                    return False
            elif curr1 != curr2:
                return False
        if stack1 and stack2:
            return False
        else:
            return True
