# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=list()
        
        def inorder(root):
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
            else:
                return None
            return root
        
        inorder(root)
        for x in range(1, len(ans)):
            if ans[x-1]>=ans[x]:
                return False
        return True