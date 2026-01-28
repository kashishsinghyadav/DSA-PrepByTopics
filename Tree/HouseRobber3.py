class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0, 0)   # (rob_this, skip_this)

            left = dfs(node.left)
            right = dfs(node.right)

            rob_this = node.val + left[1] + right[1]
            skip_this = max(left) + max(right)

            return (rob_this, skip_this)

        return max(dfs(root))
