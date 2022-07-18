# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q=list()
        res=list()
        q.append([root,TreeNode(0),0])
        while q:
            if len(res)==2:
                break
            node, parent, depth=q.pop()
            if node and (node.val==x or node.val==y):
                res.append([parent, depth])
            if node:
                q.append([node.left,node,depth+1])
                q.append([node.right,node,depth+1])
        
        return res[0][0]!=res[1][0] and res[0][1]==res[1][1]