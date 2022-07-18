# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans=""
        while head:
            ans=ans+str(head.val)
            head=head.next
        for x in range(0,len(ans)//2):
            if ans[x]!=ans[len(ans)-x-1]:
                return False
        return True