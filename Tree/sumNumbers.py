class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def findSum(root, curr):
            if root is None:
                return 0

            curr = curr * 10 + root.val

            if root.left is None and root.right is None:
                return curr

            return findSum(root.left, curr) + findSum(root.right, curr)

        return findSum(root, 0)
