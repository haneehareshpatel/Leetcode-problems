# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = list()
        ans=list()
        levelcount=1
        q.append(root)
        while q:
            level=list()
            for x in range(0,len(q)):
                node=q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                if levelcount%2==0:
                    level.reverse()
                ans.append(level)
            levelcount+=1
            
        return ans