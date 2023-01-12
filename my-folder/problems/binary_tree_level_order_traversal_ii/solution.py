# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[root]
        ans=list()
        while q:
            level=list()
            for x in range(0,len(q)):
                root = q.pop(0)
                if root:
                    level.append(root.val)
                    if root.left:
                        q.append(root.left)
                    if root.right:
                        q.append(root.right)
            if level:
                ans.append(level)
        for x in range(0,len(ans)//2):
            ans[x],ans[len(ans)-1-x]=ans[len(ans)-1-x],ans[x]
        return ans