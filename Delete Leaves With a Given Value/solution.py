# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        stack = [root]
        parent = {root: None}
        visited = set()
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if not curr.left and not curr.right and curr.val == target:
                if not parent[curr]:
                    return None
                elif parent[curr].left == curr:
                    parent[curr].left = None
                elif parent[curr].right == curr:
                    parent[curr].right = None
            if curr in visited:
                continue
            visited.add(curr)
            parent[curr.left] = curr
            parent[curr.right] = curr
            stack.append(curr)
            stack.append(curr.left)
            stack.append(curr.right)
        return root
