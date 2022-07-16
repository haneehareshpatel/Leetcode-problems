# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxans=0
        def height(root):
            if not root:
                return -1
            if root:
                left = height(root.left)
                right = height(root.right)
                if self.maxans < left+right+2:
                    self.maxans=left+right+2
                return max(left,right)+1
        height(root)
        return self.maxans