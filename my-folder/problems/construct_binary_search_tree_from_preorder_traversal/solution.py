# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.length = len(preorder)
        self.idx = 0 
        def helper(low , high):
            if self.idx==self.length:
                return None
            val = preorder[self.idx]
            if val<low or val>high:
                print("hii")
                return None
            
            self.idx+=1
            root=TreeNode(val)
            print(root)
            root.left=helper(low,val)
            
            root.right=helper(val,high)
            return root
        
        return helper(-9223372036854775807,9223372036854775807)