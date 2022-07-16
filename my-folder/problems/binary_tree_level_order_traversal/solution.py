# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=list()
        q.append(root)
        ans=list()
        while q:
            qlen=len(q)
            level=[]
            for x in range(0,qlen):
                n = q.pop(0)
                if n:
                    level.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if level:
                ans.append(level)
        return ans