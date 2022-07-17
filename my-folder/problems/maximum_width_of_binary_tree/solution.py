# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=list()
        pos=1
        maxwidth=0
        q.append([root,1])
        while q:
            level=list()
            for x in range(0,len(q)):
                node=q[0][0]
                pos=q[0][1]
                q.pop(0)
                if node:
                    level.append([node,pos])
                    q.append([node.left,pos*2])
                    q.append([node.right,pos*2+1])
            if level:
                maxwidth=max(maxwidth, level[-1][1]-level[0][1]+1)
        return maxwidth