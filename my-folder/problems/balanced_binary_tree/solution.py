# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if root is None:
                return -1
            if root:
                return max(height(root.left),height(root.right))+1
        
        if root:
            if abs(height(root.left)-height(root.right))<=1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False
        else:
            return True
            