# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        anslst=list()
        comp =""
        
        def helper(ans,root):
            if root and root.right is None and root.left is None:
                ans=ans+str(root.val)
                anslst.append(ans)
            if root:
                ans=ans+str(root.val)
                helper(ans,root.left)
                helper(ans,root.right)
        helper("",root)
        print(anslst)
        while head:
            comp=comp+str(head.val)
            head=head.next
        print(anslst)
        for x in anslst:
            if comp in x:
                return True
        return False