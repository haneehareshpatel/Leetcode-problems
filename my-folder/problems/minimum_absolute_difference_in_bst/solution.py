# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = list()
        def inorder(root):
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
            else:
                return ans
        inorder(root)
        minimum = abs(ans[0]-ans[1])
        for i in range(0,len(ans)-1):
            minimum = min(minimum,abs(ans[i]-ans[i+1]))
        minimum = min(minimum,abs(ans[-2]-ans[-1]))
        return minimum