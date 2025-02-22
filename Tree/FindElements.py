class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.s = set()
        self.s.add(root.val)  

        def reconstruct(node):
            if not node:
                return
            if node.left is not None:
                node.left.val = 2 * node.val + 1
                self.s.add(node.left.val)
                reconstruct(node.left)
            if node.right is not None:
                node.right.val = 2 * node.val + 2
                self.s.add(node.right.val)
                reconstruct(node.right)

        reconstruct(root)

    def find(self, target: int) -> bool:
        return target in self.s
