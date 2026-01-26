# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
      # gave mle
        # tot=0
        # def findNumOfPath(root,curr):
        #     nonlocal tot
        #     if root is None:
        #         return 
        #     curr+=str(root.val)
        #     if root.left is None and root.right is None:
        #         d=Counter(curr)
        #         cnt=0
        #         for i,j in d.items():
        #             if j%2==1:
        #                 cnt+=1
        #         if cnt>1:
        #             tot+=0
        #         else:
        #             tot+=1

        #     findNumOfPath(root.left,curr)
        #     findNumOfPath(root.right,curr)
        #     curr=curr[:-1]
        # findNumOfPath(root,'')
        # return tot

              ans = 0

        def dfs(node, mask):
            nonlocal ans
            if not node:
                return

            mask ^= (1 << node.val)

            if not node.left and not node.right:
                if mask & (mask - 1) == 0:
                    ans += 1
                return

            dfs(node.left, mask)
            dfs(node.right, mask)

        dfs(root, 0)
        return ans

        
