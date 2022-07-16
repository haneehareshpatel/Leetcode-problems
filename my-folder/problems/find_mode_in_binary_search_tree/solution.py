# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
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
        
        ansdict=Counter(ans)
        maxval=0
        for key,val in ansdict.items():
            if val>maxval:
                maxval=val
        fans=list()
        for key,val in ansdict.items():
            if val==maxval and key not in fans:
                fans.append(key)
        return fans
            