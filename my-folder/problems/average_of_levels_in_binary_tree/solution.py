# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        level = [root]
        ans.append(root.val/1)
        while level:
            sum_ans = 0
            count = 0
            for i in range(0, len(level)):
                root = level.pop(0)
                if root.left:
                    level.append(root.left)
                if root.right:
                    level.append(root.right)
            for i in level:
                sum_ans = sum_ans + i.val
            if len(level)!=0:
                ans.append(sum_ans/len(level))
        return ans