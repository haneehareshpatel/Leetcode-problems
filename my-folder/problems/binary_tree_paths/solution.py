# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=list()
        
        def helper(root, ansstr):
            if root is None:
                return None
            if root:
                if root.left is None and root.right is None:
                    if ansstr:
                        ansstr=ansstr+"->"+str(root.val)
                    else:
                        ansstr=str(root.val)
                    ans.append(ansstr)
                    return ans
                else:
                    if ansstr:
                        ansstr=ansstr+"->"+str(root.val)
                    else:
                        ansstr=str(root.val)
                    helper(root.left, ansstr)
                    helper(root.right, ansstr)
        helper(root,"")
        return ans