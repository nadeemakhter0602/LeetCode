# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [(root, 1)]
        result = dict()
        while len(queue) > 0:
            curr, level = queue.pop(0)
            if level in result:
                result[level].append(curr.val)
            else:
                result[level] = [curr.val]
            if curr.left != None:
                queue.append((curr.left, level + 1))
            if curr.right != None:
                queue.append((curr.right, level + 1))
        return result.values()