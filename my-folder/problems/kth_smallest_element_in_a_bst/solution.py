# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=list()
        
        def inorder(root):
            if not root:
                return None
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
            
            return root
        inorder(root)
        return ans[k-1]