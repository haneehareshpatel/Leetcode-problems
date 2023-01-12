# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = list()
        ans=list()
        if root:
            queue.append(root)
        while queue:
            level=list()
            for x in range(0,len(queue)):
                root = queue.pop(0)
                if root:
                    level.append(int(root.val))
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
            ans.append(level)
        return ans
