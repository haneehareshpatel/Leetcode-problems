# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root:
                    left = helper(root.left)
                    right = helper(root.right)
                    if right and left:
                        return 1 + min(right, left)
                    if right:
                        return 1 + right
                    else:
                        return 1+ left
            else:
                return 0
        return helper(root)