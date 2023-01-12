# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q=[root]
        ans=list()
        while q:
            level=list()
            for z in range(0,len(q)):
                root=q.pop(0)
                level.append(root.val)
                if root.left and root.right:
                    if root.left.val == x and root.right.val==y:
                        return False
                    if root.right.val == x and root.left.val==y:
                        return False
                if root:
                    if root.left:
                        q.append(root.left)
                    if root.right:
                        q.append(root.right)
            ans.append(level)
            flag=False
        for z in range(0,len(ans)):
            if x in ans[z] and y in ans[z]:
                flag=True
        return flag