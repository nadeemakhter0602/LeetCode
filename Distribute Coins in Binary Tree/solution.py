# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root, nodes, moves):
            if not root:
                return 0, 0, moves
            coinsLeft = dfs(root.left, nodes, moves)
            coinsRight = dfs(root.right, nodes, moves)
            coins = root.val + coinsLeft[0] + coinsRight[0]
            nodes = 1 + coinsLeft[1] + coinsRight[1]
            moves += abs(nodes - coins) + coinsLeft[2] + coinsRight[2]
            return coins, nodes, moves

        return dfs(root, 0, 0)[2]
