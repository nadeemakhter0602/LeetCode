# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root, moves):
            if not root:
                return 0, moves
            coinsLeft = dfs(root.left, moves)
            coinsRight = dfs(root.right, moves)
            extraCoins = root.val - 1 + coinsLeft[0] + coinsRight[0]
            moves += abs(extraCoins) + coinsLeft[1] + coinsRight[1]
            return extraCoins, moves

        return dfs(root, 0)[1]
